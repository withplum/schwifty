#!/usr/bin/env python
import json
import xlrd
import requests

URL = ("https://www.nbb.be/doc/be/be/protocol/r_fulllist_of_codes_current.xlsx")


def process(URL):
    r = requests.get(URL)
    book = xlrd.open_workbook(file_contents=r.content)
    registry = []
    skip_field = ["VRIJ", "NAV", "NAP", "-", "VRIJ - LIBRE"]
    row_count = 0

    if len(book.sheets()) == 1:
        sheet = book.sheets()[0]
    for i in range(sheet.nrows):
        if row_count > 1:
            row_count += 1
            row = sheet.row_values(i)
            column = 0
            registry_entry_template = {"bank_code": None, "bic": None, "country_code": "BE",
                                        "name": None, "primary": True, "short_name": None}
            skip_row = False
            for cell in row:
                if column == 1:
                    if cell.upper() not in skip_field:
                        registry_entry_template["bic"] = str(
                            cell.upper().replace(" ", ""))
                    else:
                        skip_row = True
                elif column == 0:
                    registry_entry_template["bank_code"] = str(cell)
                elif column == 2:
                    if cell is None:
                        pass
                    else:
                        registry_entry_template["name"] = str(cell).title()
                        registry_entry_template["short_name"] = str(cell).title()
                column += 1
            if skip_row:
                pass
            else:
                registry.append(registry_entry_template)
        else:
            row_count += 1


if __name__ == '__main__':
    with open('schwifty/bank_registry/generated_be.json', 'w') as fp:
        json.dump(process(URL), fp, indent=2)
