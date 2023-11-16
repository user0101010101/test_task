import requests


def get_form(params: dict[str, str]):
    resp = requests.post("http://localhost:10000/api/v1/get_form", params=params)
    return resp.json()["result"]


params_list = [
    {
        "contact_number": "+7 999 999 99 99",
        "order_date": "1990-02-11"
    },

    {
        "contact_number": "+7 999 999 99 99",
        "order_date": "1990-02-11",
        "description": "aaa"
    },
    {
        "user_name": "aboba",
        "phone_number": "+7 999 999 99 99",
        "birth_date": "02.11.1999",
    },
    {
        "user_name": "aboba",
        "phone_number": "+7 999 999 99 99",
        "birth_date": "02.11.1999",
        "email_address": "aboba@gmail.com"
    }
]
result = get_form(params_list[0])
print(result)
