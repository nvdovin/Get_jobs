from abstract_class import DataAnalise
from get_data import *


class CompareVacations(DataAnalise):
    def __init__(self, data):
        self.data = data
        self.sorted_data = []

    def compare_by_param(self, param):
        """ Returns sorted data by salary """
        param = " "
        while param in ["slr", "exp", "emt"]:
            param = input("""Выберите параметр сортировки:
                slr - по зарплате
                exp - по опыту
                emt - по занятости: """)
            if param in ["slr", "exp", "emt"]:
                return sorted(self.data, key=lambda x: x[param])
            else:
                print(f'Нет параметра "{param}", попробуйте еще раз')

