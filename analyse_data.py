from abstract_class import DataAnalise
from data_parser import RequestInterface
import csv
import json


class RecorderMixIn:
    @staticmethod
    def write_to_json_file(data, name):
        with open(f"text_files/{name.replace(' ', '_')}.json", "w", encoding="utf-8") as file:
            to_write = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(to_write)
        print(f'Записано в "text_files/{name}.json"')

    @staticmethod
    def write_to_csv_file(data, name):
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


class CompareVacations(RecorderMixIn, DataAnalise):
    """Получает два разных запроса и сравнивает между собой."""

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.top_data = list

    def compare_by_param(self):
        """ Сортировка по тем или иным значениям """

        param = input("""Выберите параметр сортировки:
    slr - по зарплате
    exp - по опыту
    emt - по занятости 
    none - без сортировки.
""")
        if len(self.data) > 2:
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

        elif len(self.data) == 0:
            print("Вызов пуст")

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

        sorted_data = self.compare_by_param()

        if len(sorted_data) == 2:
            for i in range(top_size):
                top_data.append(sorted_data[0][i])

            second_length = len(sorted_data[1])
            if top_size > second_length:
                top_size = second_length - 1

            for i in range(top_size):
                top_data.append(sorted_data[1][i])

        else:
            for i in range(top_size):
                top_data.append(sorted_data[i])

        self.top_data = top_data
        self.write_to_json_file(top_data, "job_search")

    def show_by_criterion(self, criterion):
        """ Визуализация по конкретному параметру """

        for vacation in self.top_data:
            print(f"{vacation['title']} - {vacation[criterion]}")

    def show_vacations_list(self):
        """ Выводим список вакансий по определенному критерию """

        print(f"""Для вывода вакансий по критериям, введите ниже критерий:
        
slr - по зарплата
exp - по опыту
emt - по занятости
Нажмите Enter для пропуска визуализации
""")

        criterion = input("Ваш выбор: ")

        if criterion in ["slr", "exp", "emp"]:
            if criterion == "slr":
                self.show_by_criterion("salary")
            elif criterion == "exp":
                self.show_by_criterion("experience")
            elif criterion == "emt":
                self.show_by_criterion("employment")
            else:
                print("Вы выбрали вариант без визуализации. ")
