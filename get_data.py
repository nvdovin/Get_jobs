import json
import os
from abstract_class import GeneralData
import requests
from get_api.superjobs_api import by_password


class HeadHunter(GeneralData):
    def __init__(self, response_text):
        self.response_text = response_text
        self.url = "https://api.hh.ru/vacancies"

    def get_main_data(self, page=0):
        data = requests.get(self.url, params={
            "page": page,
            "text": self.response_text
        })
        return data.json()

    def __repr__(self):
        return "Класс получения данных с HeadHunter"

    def __str__(self):
        return f"{self.get_main_data(0)}"


class SuperJob(GeneralData):
    def __init__(self, keyword):
        self.keyword = keyword
        self.access_token = os.getenv("SJ_ACCESS_TOKEN")
        self.secret_key = os.getenv("SJ_SECRET_KEY")

    def get_main_data(self):
        data = requests.get(
            "https://api.superjob.ru/2.0/vacancies/",
            params={"keyword": self.keyword},
            headers={"X-Api-App-Id": self.secret_key}
        )
        return data

    def __str__(self):
        return f"{self.get_main_data().text}"

    def __repr__(self):
        return "Класс получения данных с SuperJob"
