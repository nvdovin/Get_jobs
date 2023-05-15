from abstract_class import UserActions


class Actions(UserActions):
    def get_users_action(self):
        """
        Эта функция позволяет выбрать тип действия для массива данных
        :return: Тип действия
        """

        print(f"""
Выберите, что вы хотите сделать с полученными данными:
    sort - сортировать 
    top - вывести топ вакансий
""")
        action_type = " "
        while action_type not in ["sort", "top"]:
            action_type = input("Выберите вариант действия: ")

        return action_type

    def get_user_response(self):
        """
        Эта функция позволяет сформировать поисковый запрос.
        :return: Запрос
        """

        return input("Ваш поисковый запрос: ")
