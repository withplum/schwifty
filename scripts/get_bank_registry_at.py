import csv
import json

import requests


URL = "https://www.oenb.at/docroot/downloads_observ/sepa-zv-vz_gesamt.csv"


def process():
    with requests.get(URL, stream=True) as fp:
        csvfile = csv.reader([line.decode("latin1") for line in fp.iter_lines()], delimiter=";")

    return [
        {
            "country_code": "AT",
            "primary": True,
            "bic": row[18].strip().upper(),
            "bank_code": row[2].strip().rjust(5, "0"),
            "name": row[6].strip(),
            "short_name": row[6].strip(),
        }
        for i, row in enumerate(csvfile)
        if i >= 6 and len(row) >= 19
    ]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_at.json", "w") as fp:
        json.dump(process(), fp, indent=2)
