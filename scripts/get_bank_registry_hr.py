#!/usr/bin/env python
import json
import xlrd
import requests

URL = (
    "https://www.hnb.hr/documents/20182/121798/tf-pp-ds-vbb-xlsx-e-vbb.xlsx/"
    "06982c63-13e3-4aa0-846d-afb7956ee731"
)


def process():
    registry = []

    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)

    for row in list(sheet.get_rows())[4:]:
        name, bank_code, bic = row[1:]
        registry.append(
            {
                "country_code": "HR",
                "primary": True,
                "bic": bic.value.upper().replace(" ", ""),
                "bank_code": int(bank_code.value),
                "name": name.value,
                "short_name": name.value,
            }
        )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_hr.json", "w") as fp:
        json.dump(process(), fp, indent=2)
