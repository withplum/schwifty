import json
import csv
import requests

URL = "https://www.oenb.at/docroot/downloads_observ/sepa-zv-vz_gesamt.csv"


def process():
    registry = []
    with requests.get(URL, stream=True) as csvfile:
        count = 0
        for row in csvfile.iter_lines():
            if count != 6:
                count += 1
            elif len(row.decode("latin1").split(";")) != 21:
                continue
            else:
                registry.append(
                    {
                        "country_code": "AT",
                        "primary": True,
                        "bic": row.decode("latin1").split(";")[18].strip().upper(),
                        "bank_code": row.decode("latin1").split(";")[2].strip(),
                        "name": row.decode("latin1").split(";")[6].strip(),
                        "short_name": row.decode("latin1").split(";")[6].strip(),
                    }
                )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_at.json", "w") as fp:
        json.dump(process(), fp, indent=2)
