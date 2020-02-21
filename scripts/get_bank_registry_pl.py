import json
import csv
import requests

URL = "https://ewib.nbp.pl/plewibnra?dokNazwa=plewibnra.txt"


def process():
    registry = []
    with requests.get(URL, stream=True) as txtfile:
        for row in txtfile.iter_lines():
            if len(row.decode("latin1").split("\t")) != 33:
                continue
            else:
                registry.append(
                    {
                        "country_code": "PL",
                        "primary": True,
                        "bic": row.decode("latin1").split("\t")[19].strip().upper(),
                        "bank_code": row.decode("latin1").split("\t")[4].strip(),
                        "name": row.decode("latin1").split("\t")[1].strip(),
                        "short_name": row.decode("latin1").split("\t")[1].strip(),
                    }
                )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_pl.json", "w") as fp:
        json.dump(process(), fp, indent=2)
