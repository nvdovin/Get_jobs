import requests
import json
import os


url = "https://api.superjob.ru/"
secret_code = os.getenv("SJ_SECRET_CODE")


def by_password():
    req = requests.get(
        "https://api.superjob.ru/2.0/oauth2/password/",
        params={
            "login": "vdovin-na@yandex.ru",
            "password": "Ghjcnj12!",
            "client_id": 2437,
            "client_secret": secret_code
        }
    )
    return req


req = by_password()

with open("superjobs_api.txt", "w", encoding="utf-8") as file:
    file.write(json.dumps(req.json(), indent=4))

