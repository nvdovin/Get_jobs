from get_data import *
from user_actions import *
import json
import csv


class Recorder:
    @staticmethod
    def record(data, name: str, record_type: str = "json"):
        if record_type == "json":
            with open(f"text_files/{name.replace(' ', '_')}.json", "w", encoding="utf-8") as file:
                to_write = json.dumps(data, indent=4, ensure_ascii=False)
                file.write(to_write)
            print(f'Записано в "text_files/{name}.json"')

        elif record_type == "cvs":
            fields = {
                "title": "Профессия",
                "professional_roles": "Должность",
                "salary": "Зарплата",
                "area": "Местонахождение",
                "snippet": "Краткое описание",
                "experience": "Опыт работы",
                "employment": "Занятость",
                "url": "Ссылка"
            }

            with open(f"text_files/{name.replace(' ', '_')}.csv", "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fields)
                writer.writeheader()
                writer.writerows(data)


class HeadHunterParser(HeadHunter, Recorder):
    def __init__(self, response_text):
        super().__init__(response_text)
        self.response_text = input("Введите текст запроса: ")
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
        self.record(self.total_data, self.response_text)
        return self.total_data


hp = HeadHunterParser("P")
hp.get_parsed_dictionary()
