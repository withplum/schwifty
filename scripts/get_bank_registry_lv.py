#!/usr/bin/env python
import json
import xlrd
import requests

URL = "https://www.bank.lv/images/stories/pielikumi/makssist/bic_saraksts_22.01.2020_eng.xls"


def process():
    registry = []

    book = xlrd.open_workbook(file_contents=requests.get(URL).content)
    sheet = book.sheet_by_index(0)

    for row in list(sheet.get_rows())[2:]:
        name, bank_code, bic = row[1:]
        registry.append(
            {
                "country_code": "LV",
                "primary": True,
                "bic": bic.value.upper(),
                "bank_code": bank_code.value[4:8],
                "name": name.value,
                "short_name": name.value,
            }
        )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_lv.json", "w") as fp:
        json.dump(process(), fp, indent=2)
