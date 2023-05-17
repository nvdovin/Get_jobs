from abstract_class import GeneralData
import requests


class HeadHunter(GeneralData):
    def __init__(self, response_text: str):
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
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.secret_key = "v3.r.137548679.e52320967352ba00b5012258aae81413a76d0fbb.49831d30dacf09d700882a6b684a49a5d518d66e"

    def get_main_data(self):
        data = requests.get(
            "https://api.superjob.ru/2.0/vacancies/",
            params={"keyword": self.keyword,
                    "order_field": "payment"},
            headers={"X-Api-App-Id": self.secret_key}
        )
        return data.json()

    def __str__(self):
        return f"{self.get_main_data().text}"

    def __repr__(self):
        return "Класс получения данных с SuperJob"
