#!/usr/bin/env python
import json
import xlrd
import requests

URL = "https://www.nbb.be/doc/be/be/protocol/r_fulllist_of_codes_current.xlsx"


def process():
    registry = []
    skip_names = ["NAV", "VRIJ", "NAP", "NYA", "VRIJ - LIBRE", "-"]
    book = xlrd.open_workbook(file_contents=requests.get(URL).content)

    try:
        sheet = book.sheet_by_index(0)
        for row in list(sheet.get_rows())[2:]:
            bank_code, bic, name, second_name = row[:4]
            if bic.value.upper() in skip_names:
                continue
            if name.value != "":
                registry.append({
                    "country_code": "BE",
                    "primary": True,
                    "bic": bic.value.upper().replace(" ", ""),
                    "bank_code": bank_code.value,
                    "name": name.value,
                    "short_name": name.value,
                })
            else:
                registry.append({
                    "country_code": "BE",
                    "primary": True,
                    "bic": bic.value.upper().replace(" ", ""),
                    "bank_code": bank_code.value,
                    "name": second_name.value,
                    "short_name": second_name.value,
                })
        return registry
    except IndexError:
        raise


if __name__ == '__main__':
    with open('schwifty/bank_registry/generated_be.json', 'w') as fp:
        json.dump(process(), fp, indent=2)
