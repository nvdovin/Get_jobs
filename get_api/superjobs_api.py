"""
POST /2.0/favorites/ HTTP/1.1
    Host: api.superjob.ru
    X-Api-App-Id: yourAppSecretKey
    Authorization: Bearer r.000000010000001.example.access_token
    Content-Type: application/x-www-form-urlencoded
"""
import requests


url = "https://api.superjob.ru/"
secret_code = "v3.r.137548679.e52320967352ba00b5012258aae81413a76d0fbb.49831d30dacf09d700882a6b684a49a5d518d66e"


def post_method():
    request = requests.post(f"{url}/2.0/favorites/", params={
        "Host": "api.superjob.ru",
        "X-Api-App-Id": secret_code,
        "Authorization": "Bearer r.000000010000001.example.access_token",
        "Content-Type": "application/x-www-form-urlencoded"
    })
    return request


def get_method():
    """
    GET https://api.superjob.ru/2.0/user/current/
    Host: api.superjob.ru
    X-Api-App-Id: v3.r.137548679.e52320967352ba00b5012258aae81413a76d0fbb.49831d30dacf09d700882a6b684a49a5d518d66e
    Authorization: Bearer r.000000000000001.example.token
    """
    request = requests.get("https://api.superjob.ru/2.0/user/current/", params={
        "Host": "api.superjob.ru",
        "X-Api-App-Id": secret_code,
        "Authorization": "Bearer r.000000000000001.example.token"
    })
    return request


def authorization():
    """
    GET https://api.superjob.ru/2.0/user/current/
    Host: api.superjob.ru
    X-Api-App-Id: yourAppSecretKey
    Authorization: Bearer r.000000000000001.example.token
    """

    request = requests.get("https://api.superjob.ru/2.0/user/current/",
                           params={
                               "Host": "api.superjob.ru",
                               "X-Api-App-Id": secret_code,
                               "Authorization": "Bearer r.000000000000001.example.token"
                           }
    )
    return request


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


def authorize_code():
    req = requests.get(
        "https://www.superjob.ru/authorize/", params={
            "client_id": 2437,
            "redirect_uri": "https://get_jobs"
        }
    )
    return req


req = authorize_code()

with open("superjobs_code.html", "w") as file:
    file.write(req.text)

print(req.text)
