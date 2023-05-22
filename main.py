from analyse_data import RequestInterface, CompareVacations


if __name__ == "__main__":
    data = RequestInterface().get_data()
    mn = CompareVacations(data)
    top_data = mn.output_top()
    mn.show_vacations_list()

