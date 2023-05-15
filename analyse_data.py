from abstract_class import DataAnalise
from get_data import *


class CompareVacations(DataAnalise):
    def __init__(self, data):
        self.data = data
        self.sorted_data = self.compare_by_param()

    def compare_by_param(self, param=10):
        """ Returns sorted data by salary """

        param = " "
        while param in ["slr", "exp", "emt"]:
            param = input("""Выберите параметр сортировки:
                slr - по зарплате
                exp - по опыту
                emt - по занятости: """)
            if param in ["slr", "exp", "emt"]:
                return sorted(self.data, key=lambda x: x[param], reverse=True)
            else:
                print(f'Нет параметра "{param}", попробуйте еще раз')

    def output_top(self, top_size: int):
        top_size = input("Вывод топ из ... вакансий")
        while top_size.isalpha():
            print("Это не число")
            top_size = input("Вывод топ из ... вакансий")

        int(top_size)
        with open("top_vacations.txt", "w", encoding="utf-8") as top_list:
            for item in self.sorted_data:
                top_list.write(f"{item} \n")

        print("Данные записаны в файл 'top_vacations.txt' ")

