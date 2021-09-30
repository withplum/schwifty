#!/usr/bin/env python
import json

import requests
import xlrd


URL = (
    "https://www.finanssiala.fi/wp-content/uploads/2021/03/"
    "Finnish_monetary_institution_codes_and_BICs_in_excel_format.xlsx"
)


def process():
    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)

    return [
        {
            "country_code": "FI",
            "primary": True,
            "bic": bic.value.upper().strip(),
            "bank_code": bank_code.value,
            "name": name.value,
            "short_name": name.value,
        }
        for bank_code, bic, name in list(sheet.get_rows())[2:]
        if bank_code.value != ""
    ]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_fi.json", "w") as fp:
        json.dump(process(), fp, indent=2)
