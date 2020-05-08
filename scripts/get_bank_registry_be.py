#!/usr/bin/env python
import json

import requests
import xlrd


URL = "https://www.nbb.be/doc/be/be/protocol/r_fulllist_of_codes_current.xlsx"


def process():
    registry = []
    skip_names = ["NAV", "VRIJ", "NAP", "NYA", "VRIJ - LIBRE", "-"]

    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)

    for row in list(sheet.get_rows())[2:]:
        bank_code, bic, name, second_name = row[:4]
        if bic.value.upper() in skip_names:
            continue
        registry.append(
            {
                "country_code": "BE",
                "primary": True,
                "bic": bic.value.upper().replace(" ", ""),
                "bank_code": bank_code.value,
                "name": name.value or second_name.value,
                "short_name": name.value or second_name.value,
            }
        )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_be.json", "w") as fp:
        json.dump(process(), fp, indent=2)
