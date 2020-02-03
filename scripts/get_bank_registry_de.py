#!/usr/bin/env python
import json

import requests


FIELD_LENGTHS = {
    "bank_code": 8,
    "feature": 1,
    "name": 58,
    "postal_code": 5,
    "place": 35,
    "short_name": 27,
    "pan": 5,
    "bic": 11,
    "check_digit_method": 2,
    "record_number": 6,
    "mod_number": 1,
    "tbd": 1,
    "successor_bank_code": 8,
}
URL = (
    "https://www.bundesbank.de/resource/blob/"
    "602632/b8ada8f2b30c6ede5d237be9b932a014/mL/blz-aktuell-txt-data.txt"
)


def get_raw():
    return requests.get(URL).content.decode(encoding="latin1")


def parse(raw):
    for line in raw.split("\n"):
        if not line:
            continue
        record = {}
        offset = 0
        for field, length in FIELD_LENGTHS.items():
            record[field] = line[offset : offset + length].strip()
            offset = offset + length
        yield record


def process(records):
    fieldnames = ("bank_code", "name", "short_name", "bic")
    registry = []
    for record in records:
        if not record["bank_code"]:
            continue

        cleaned = {k: v for k, v in record.items() if k in fieldnames}
        cleaned["primary"] = record["feature"] == "1"
        cleaned["country_code"] = "DE"

        if cleaned["bic"]:
            registry.append(cleaned)
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_de.json", "w") as fp:
        json.dump(process(parse(get_raw())), fp, indent=2)
