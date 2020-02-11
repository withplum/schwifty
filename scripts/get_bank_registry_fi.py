#!/usr/bin/env python
import json
import xlrd
import requests

URL = "https://www.finanssiala.fi/maksujenvalitys/dokumentit/Finnish_monetary_institution_codes_and_BICs_in_excel_format.xlsx"


def process():
    registry = []

    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)

    for row in list(sheet.get_rows())[2:]:
        bank_code, bic, name = row
        if bank_code.value != "":
            registry.append(
                {
                    "country_code": "FI",
                    "primary": True,
                    "bic": bic.value.upper(),
                    "bank_code": bank_code.value,
                    "name": name.value,
                    "short_name": name.value,
                }
            )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_fi.json", "w") as fp:
        json.dump(process(), fp, indent=2)
