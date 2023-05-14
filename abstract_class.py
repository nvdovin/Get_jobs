from abc import ABC, abstractmethod


class DataWork(ABC):
    @abstractmethod
    def writing_to_json(self):
        pass

    @abstractmethod
    def writing_to_csv(self):
        pass

    @abstractmethod
    def parsing_to_dictionaries(self):
        pass


class DataAnalise(ABC):
    @abstractmethod
    def compare_by_param(self, param):
        pass


class UserActions(ABC):
    @abstractmethod
    def get_user_response(self):
        pass

    def get_users_action(self):
        pass


class GeneralData(ABC):
    @abstractmethod
    def get_main_data(self):
        pass