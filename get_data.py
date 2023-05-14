import os
from abstract_class import GeneralData
import requests
import json
from get_api.superjobs_api import by_password


class HeadHunter(GeneralData):
    def __init__(self, response_text):
        self.response_text = response_text
        self.url = "https://api.hh.ru/vacancies"

    def get_main_data(self, page):
        data = requests.get(self.url, params={
            "page": page,
            "text": self.response_text
        })
        return data.json()

    def __repr__(self):
        return "Класс получения данных с HeadHanter"

    def __str__(self):
        return f"{self.get_main_data(0)}"


class SuperJob(GeneralData):
    def __init__(self, keyword):
        self.keyword = keyword
        self.access_token = os.getenv("SJ_ACCESS_TOKEN")
        self.secret_key = os.getenv("SJ_SECRET_KEY")

    def get_main_data(self):
        data = requests.post(
            "https://api.superjob.ru/2.0/vacancies/", params={
                "keyword": self.keyword
            },
            auth=by_password()
        )
        return data

    def write(self):
        with open("content.html") as f:
            f.write(self.get_main_data().text)

    def __str__(self):
        return f"{self.get_main_data().text}"

    def __repr__(self):
        return "Класс получения данных с SuperJob"


sj = SuperJob("python")
sj.write()

# hh = HeadHunter("python")
# print(hh)
