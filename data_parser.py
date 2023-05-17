from get_data import *
from user_actions import *
import json
import csv


class HeadHunterParser(HeadHunter):
    def __init__(self, response_text):
        super().__init__(response_text)
        self.total_data = []

    def get_parsed_dictionary(self):
        hh = HeadHunter(self.response_text)
        pages = hh.get_main_data()["pages"]

        for page in range(pages):
            for item in hh.get_main_data(page)["items"]:
                title = item["name"]
                city = item["area"]["name"]

                try:
                    salary = f"от {item['salary']['to']} до {item['salary']['to']} {item['salary']['currency']}"
                    if item['salary']['to'] is None:
                        salary = f"от {item['salary']['from']} {item['salary']['currency']}"
                    elif item['salary']['from'] is None:
                        salary = f"до {item['salary']['to']} {item['salary']['currency']}"
                except:
                    salary = "Нет данных"

                url = item["alternate_url"]

                try:
                    snippet = item["snippet"]["requirement"].replace("<highlighttext>", "").replace("</highlighttext>",
                                                                                                    "")
                except AttributeError:
                    snippet = item["snippet"]["requirement"]

                experience = item["experience"]["name"]
                employment = item["employment"]["name"]
                professional_roles = item["professional_roles"][0]["name"]

                self.total_data.append(
                    {
                        "title": title,
                        "professional_roles": professional_roles,
                        "salary": salary,
                        "area": city,
                        "snippet": snippet,
                        "experience": experience,
                        "employment": employment,
                        "url": url
                    }
                )

        return self.total_data


class SuperJobParser(SuperJob):
    def __init__(self, keyword):
        super().__init__(keyword)
        self.keyword = keyword

    def get_parsed_dictionary(self):
        sj = SuperJob(self.keyword)
        objects = sj.get_main_data()["objects"]
        total_data = []

        for obj in objects:
            professional_roles = []
            title = obj["profession"]

            for role in obj["catalogues"][0]["positions"]:
                professional_roles.append(role["title"])

            if obj['payment_to'] == 0 and obj['payment_from'] != 0:
                salary = f"от {obj['payment_from']}"
            elif obj['payment_to'] != 0 and obj['payment_from'] == 0:
                salary = f"до {obj['payment_to']}"
            elif obj['payment_to'] == 0 and obj['payment_from'] == 0:
                salary = f"Нет данных"
            else:
                salary = f"от {obj['payment_from']} до {obj['payment_to']}"

            area = obj["town"]["title"]
            snippet = obj["candidat"]
            experience = obj["experience"]["title"]
            employment = obj["type_of_work"]["title"]
            url = obj["link"]

            total_data.append(
                {
                    "title": title,
                    "professional_roles": professional_roles,
                    "salary": salary,
                    "area": area,
                    "snippet": snippet,
                    "experience": experience,
                    "employment": employment,
                    "url": url
                }
            )

        return total_data


class GetRequest(SuperJobParser, HeadHunterParser):
    """ Объединяющий класс для всех запросов"""
    def __init__(self):
        super().__init__(self)
        self.request = input("Введите запрос: ")
        self.sp = SuperJobParser(self.request)
        self.hp = HeadHunterParser(self.request)

    @property
    def platform(self):
        platform = input("Выберите ресурс: hh, sj, либо нажмите на Enter для выбора всех платформ")
        if platform == "hh":
            return "hh"
        elif platform == "sj":
            return "sj"
        else:
            return "all"

    def get_data(self):
        if self.platform == "hh":
            return self.hp.get_parsed_dictionary()
        elif self.platform == "sj":
            return self.sp.get_parsed_dictionary()
        elif self.platform == "all":
            return [self.hp.get_parsed_dictionary(), self.sp.get_parsed_dictionary()]

    def __str__(self):
        return f"Вывод распарсенных данных для последующего анализа"
