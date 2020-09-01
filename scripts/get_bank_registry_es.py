import json
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


URL = "https://www.iban.es/bancos/"
titles = {
    "Código de entidad (código de banco)": "bank_code",
    "Código BIC Banco (Codigo SWIFT)": "bic",
    "Denominación legal del Banco": "name",
    "Nombre Comercial (abreviado)": "short_name",
}


def get_bank_details(path):
    soup = BeautifulSoup(requests.get(urljoin(URL, path)).content, "html.parser")
    rows = soup.select("div.about-content-text table tr")

    record = {"country_code": "ES", "primary": True}
    for row in rows:
        cells = row.find_all("td")
        if len(cells) != 2:
            continue
        title, value = cells[0].text.strip(), cells[1].text.strip()
        key = titles.get(title)
        if key:
            record[key] = value
    return record


def process():
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    paths = [a["href"] for a in soup.select("h6.portfolio-title a")]
    print(f"Fetched {len(paths)} bank records")
    return [get_bank_details(path) for path in paths]


if __name__ == "__main__":
    with open("schwifty/bank_registry/generated_es.json", "w") as fp:
        json.dump(process(), fp, indent=2)
