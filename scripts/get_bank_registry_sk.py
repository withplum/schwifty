import csv
import json

import requests

from schwifty import BIC


URL = "https://www.nbs.sk/_img/Documents/_PlatobneSystemy/EUROSIPS/Directory_IC_DPS_SR.csv"


def process():
    with requests.get(URL, stream=True) as fp:
        csvfile = csv.reader([line.decode("cp1250") for line in fp.iter_lines()], delimiter=";")
    registry = []
    for row in csvfile:
        bic = row[2].strip().upper()
        if bic and not BIC(bic, allow_invalid=True).is_valid:
            continue
        registry.append(
            {
                "country_code": "SK",
                "primary": True,
                "bic": bic,
                "bank_code": row[0].strip().zfill(4),
                "name": row[1].strip(),
                "short_name": row[1].strip(),
            }
        )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_sk.json", "w") as fp:
        json.dump(process(), fp, indent=2)
