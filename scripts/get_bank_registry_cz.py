import json
import csv
import requests

URL = "https://www.cnb.cz/cs/platebni-styk/.galleries/ucty_kody_bank/download/kody_bank_CR.csv"


def process():
    registry = []
    firstline = True

    with requests.get(URL, stream=True) as csvfile:
        for row in csvfile.iter_lines():
            if firstline:
                firstline = False
            else:
                bank_code, name, bic = row.decode("latin1").split(";")[0:3]
                registry.append(
                    {
                        "country_code": "CZ",
                        "primary": True,
                        "bic": bic.upper(),
                        "bank_code": bank_code,
                        "name": name,
                        "short_name": name,
                    }
                )
        return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_cz.json", "w") as fp:
        json.dump(process(), fp, indent=2)
