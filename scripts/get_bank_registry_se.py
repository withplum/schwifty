#!/usr/bin/env python
import json

import requests
import xlrd


# https://www.swedishbankers.se/fraagor-vi-arbetar-med/betalningar/ny-nordisk-betalningsinfrastruktur/iban-och-svenskt-nationellt-kontonummer/
URL = (
    "https://www.swedishbankers.se/media/4863/"
    "kalkylblad-i-iban-och-svenskt-nationellt-kontonummer-2021-02-16.xlsx"
)


def process():
    registry = []

    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)

    for row in list(sheet.get_rows())[3:]:
        bank_code, bic, name = row[:3]
        registry.append(
            {
                "country_code": "SE",
                "primary": True,
                "bic": bic.value.upper(),
                "bank_code": str(bank_code.value).split(".", 1)[0],
                "name": name.value.strip(),
                "short_name": name.value.strip(),
            }
        )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_se.json", "w") as fp:
        json.dump(process(), fp, indent=2)
