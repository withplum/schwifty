import csv
import json
import sys


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fp:
        all_fieldnames = [
            'bank_code', 'feature', 'name', 'postal_code', 'place', 'short_name', 'pan', 'bic',
            'check_digit_method', 'record_number', 'mod_number', 'tbd', 'successor_bank_code']
        data = csv.DictReader(fp, all_fieldnames, delimiter=';')

        fieldnames = ('bank_code', 'name', 'short_name', 'bic', 'tbd')
        cleaned = []
        for row in data:
            if not row['bank_code'].strip():
                continue
            for key, value in row.items():
                if key == 'feature':
                    row['primary'] = value.strip() == '1'
                if key not in fieldnames:
                    del row[key]
                    continue
                row[key] = value.strip()
            row['country_code'] = 'DE'
            if row['bic']:
                cleaned.append(row)

    with open('schwifty/bank-registry.json', 'w') as fp:
        json.dump(cleaned, fp, indent=2)
