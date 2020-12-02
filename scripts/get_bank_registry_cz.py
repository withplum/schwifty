import csv
import json

import requests


URL = "https://www.cnb.cz/cs/platebni-styk/.galleries/ucty_kody_bank/download/kody_bank_CR.csv"


def process():
    with requests.get(URL, stream=True) as fp:
        csvfile = csv.reader([line.decode("latin1") for line in fp.iter_lines()], delimiter=";")
    return [
        {
            "country_code": "CZ",
            "primary": True,
            "bic": row[2].strip().upper(),
            "bank_code": row[0].strip(),
            "name": row[1].strip(),
            "short_name": row[1].strip(),
        }
        for i, row in enumerate(csvfile)
        if i >= 1 and row
    ]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_cz.json", "w") as fp:
        json.dump(process(), fp, indent=2)
