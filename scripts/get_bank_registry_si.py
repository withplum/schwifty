import json
import requests

URL = (
    "https://www.bsi.si/ckfinder/connector?command=Proxy&lang=sl&type=Files&"
    "currentFolder=%2FPla%C4%8Dilni%20sistemi%2FSeznam%20identifikacijskih%20oznak%20PPS%2F&"
    "hash=6ce6c512ea433a7fc5c8841628e7696cd0ff7f2b&fileName=List-of-identifiers-of-PSP.txt"
)


def process():
    registry = []
    firstline = True

    with requests.get(URL, stream=True) as txtfile:
        for row in txtfile.iter_lines():
            if firstline:
                firstline = False
            elif len(row.decode("latin1").split(";")) != 6:
                continue
            else:
                bank_code, name = row.decode("latin1").split(";")[:2]
                registry.append(
                    {
                        "country_code": "SI",
                        "primary": True,
                        "bic": row.decode("latin1").split(";")[5].upper(),
                        "bank_code": bank_code,
                        "name": name,
                        "short_name": name,
                    }
                )
    return registry


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_si.json", "w") as fp:
        json.dump(process(), fp, indent=2)
