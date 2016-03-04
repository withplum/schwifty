import csv
import json
import re

from bs4 import BeautifulSoup
import requests


url = 'https://www.swift.com/standards/data-standards/iban'


def get_raw():
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    link = soup.find('a', attrs={'data-title': 'IBAN Registry TXT'})
    return requests.get(link['href']).content


def clean(raw):
    chars = ' \t\n\r;:\'"'
    return [{key.strip(chars).lower(): value.strip(chars) for key, value in line.items()}
            for line in raw]


def parse_positions(bban_length, spec):
    pattern = r'(.*?)(\d+)\s*(?:-|to)\s*(\d+)'
    matches = re.findall(pattern, spec)
    positions = {'bank_code': [0, 0], 'branch_code': [0, 0], 'account_code': [0, 0]}

    def match_to_range(match):
        return [int(match[1]) - 1, int(match[2])]

    positions['account_code'] = [0, bban_length]
    if matches:
        positions['bank_code'] = match_to_range(matches[0])
        positions['account_code'][0] = positions['bank_code'][1]
    if len(matches) > 1 and 'Branch' in matches[1][0]:
        positions['branch_code'] = match_to_range(matches[1])
        positions['account_code'][0] = positions['branch_code'][1]
    else:
        positions['branch_code'] = [positions['bank_code'][1], positions['bank_code'][1]]
    return positions


if __name__ == '__main__':
    raw = get_raw()
    data = csv.DictReader(raw.splitlines(), delimiter='\t', quotechar='"')
    registry = {}
    for row in clean(data):
        codes = re.findall(r'[A-Z]{2}', row['country code as defined in iso 3166'])
        entry = {
            'bban_spec': row['bban structure'],
            'bban_length': row['bban length'],
            'iban_spec': re.match(r'[A-Za-z0-9!]+', row['iban structure']).group(0),
            'iban_length': int(row['iban length']),
        }
        if entry['bban_spec'] == 'Not in use':
            entry['bban_spec'] = re.sub(r'[A-Z]{2}2!n', '', entry['iban_spec'])
        entry['bban_spec'] = entry['bban_spec'].replace(' ', '')

        if entry['bban_length'] == 'Not in use':
            entry['bban_length'] = entry['iban_length'] - 4
        else:
            entry['bban_length'] = int(entry['bban_length'])

        entry['positions'] = parse_positions(
            entry['bban_length'],
            row['bank identifier position within the bban'])

        for code in codes:
            registry[code] = entry

    with open('schwifty/iban-registry.json', 'w+') as fp:
        json.dump(registry, fp, indent=2)
