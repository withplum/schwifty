#!/usr/bin/env python
import json

import requests
import xlrd


URL = "https://www.hnb.hr/documents/20182/121798/tf-pp-ds-vbb-xlsx-e-vbb.xlsx/"


def process():
    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)
    return [
        {
            "country_code": "HR",
            "primary": True,
            "bic": bic.value.upper().replace(" ", ""),
            "bank_code": str(int(bank_code.value)),
            "name": name.value,
            "short_name": name.value,
        }
        for _, name, bank_code, bic in list(sheet.get_rows())[4:]
    ]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_hr.json", "w") as fp:
        json.dump(process(), fp, indent=2)
