import requests


def get_form(params: dict[str, str]):
    resp = requests.post("http://localhost:10000/api/v1/get_form", params=params)
    return resp.json()["result"]


params = {
    "contact_number": "+7 999 999 99 99",
    "order_date": "1990-02-11"
}

params = {
    "contact_number": "+7 999 999 99 99",
    "order_date": "1990-02-11",
    "description": "aaa"
}
result = get_form(params)
print(result)
