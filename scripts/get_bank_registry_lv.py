#!/usr/bin/env python
import json

import requests
import xlrd


URL = "https://www.bank.lv/images/stories/pielikumi/makssist/bic_saraksts_22.01.2020_eng.xls"


def process():
    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)
    return [
        {
            "country_code": "LV",
            "primary": True,
            "bic": bic.value.upper(),
            "bank_code": bic.value[:4],
            "name": name.value,
            "short_name": name.value,
        }
        for _id, name, _iban_structure, bic in list(sheet.get_rows())[2:]
    ]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_lv.json", "w") as fp:
        json.dump(process(), fp, indent=2)
