from abstract_class import DataAnalise
from data_parser import *
import csv
import json


class RecorderMixin:
    """..."""

    def __write_to_json_file(self):
        pass

    def __write_to_csv_file(self):
        pass

    def __write_to_dict(self):
        pass

    @staticmethod
    def record(data: list, name: str, record_type: str = "json"):

        if record_type == "json":  # def read_file()
            with open(f"text_files/{name.replace(' ', '_')}.json", "w", encoding="utf-8") as file:
                to_write = json.dumps(data, indent=4, ensure_ascii=False)
                file.write(to_write)
            print(f'Записано в "text_files/{name}.json"')

        if record_type == "csv":
            fields = [
                "title",
                "professional_roles",
                "salary",
                "area",
                "snippet",
                "experience",
                "employment",
                "url"
            ]
            try:
                if type(data[0]["professional_roles"]) is list:
                    data[0]["professional_roles"] = "; ".join(data[0]["professional_roles"])

                    with open(f"text_files/{name.replace(' ', '_')}.csv", "w", newline="") as csv_file:
                        writer = csv.DictWriter(csv_file, fields)
                        writer.writeheader()
                        writer.writerows(data[0])
                        writer.writerows(data[1])

            except IndexError:
                print("Нечего записывать. Пустой запрос")

        elif record_type == "none":
            print(json.dumps(data, indent=4, ensure_ascii=False))
            return


class CompareVacations(RecorderMixin, DataAnalise):
    """Получает два разных запроса и сравнивает между собой."""

    def __init__(self, data):
        super().__init__()
        self.data = data

    def compare_by_param(self):
        """ Сортировка по тем или иным значениям """
        param = str
        while param not in ["slr", "exp", "emt"]:
            param = input("""Выберите параметр сортировки:
    slr - по зарплате
    exp - по опыту
    emt - по занятости 
    none - без сортировки.
""")
            if type(self.data) is dict:
                if param in ["slr", "exp", "emt"]:
                    if param == "slr":
                        return sorted(self.data, key=lambda x: x["salary"], reverse=True)
                    elif param == "exp":
                        return sorted(self.data, key=lambda x: x["experience"], reverse=True)
                    elif param == "emt":
                        return sorted(self.data, key=lambda x: x["employment"], reverse=True)

                else:

                    print(f'Нет параметра "{param}", попробуйте еще раз')
                    return self.data

            else:
                if param not in ["slr", "exp", "emt"]:
                    hh = self.data[0]
                    sj = self.data[1]
                else:
                    if param == "slr":
                        hh = sorted(self.data[0], key=lambda x: x["salary"], reverse=True)
                        sj = sorted(self.data[1], key=lambda x: x["salary"], reverse=True)
                    elif param == "exp":
                        hh = sorted(self.data[0], key=lambda x: x["experience"], reverse=True)
                        sj = sorted(self.data[1], key=lambda x: x["experience"], reverse=True)
                    elif param == "emt":
                        hh = sorted(self.data[0], key=lambda x: x["employment"], reverse=True)
                        sj = sorted(self.data[1], key=lambda x: x["employment"], reverse=True)

                return (hh, sj)

    def output_top(self):
        top_size = input("Вывод топ из ... вакансий: ")
        while top_size.isalpha():
            print("Это не число")
            top_size = input("Вывод топ из ... вакансий: ")
        top_size = int(top_size)
        top_data = []

        if len(self.compare_by_param()) == 2:
            for i in range(top_size):
                top_data.append(self.compare_by_param()[0][i])
            for i in range(top_size):
                top_data.append(self.compare_by_param()[1][i])

        else:
            for i in range(top_size):
                top_data.append(self.compare_by_param()[i])

        self.record(top_data, self.request)

