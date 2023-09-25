from abc import ABC, abstractmethod
import copy
import requests
import json


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def change_date(self):
        pass

    @abstractmethod
    def add_word(self):
        pass

    @abstractmethod
    def add_area(self):
        pass

    @abstractmethod
    def load_all_areas(self):
        pass


class HeadHunter_API(API):

    HH_API_URL = 'https://api.hh.ru/vacancies'
    HH_API_URL_AREAS = 'https://api.hh.ru/areas'

    param_zero ={
        'text': 'python',
        'per_page': 100,
        'area': 47,
        'data': 14
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_zero)
        pass

    def get_vacancies(self):
        response = requests.get(self.HH_API_URL, self.param)
        return response.json()["items"]
    def change_date(self):
        pass

    def add_word(self):
        pass

    def add_area(self):
        pass

    def load_all_areas(self):
        response = requests.get(self.HH_API_URL_AREAS)
        return response.json()

class SuperJob_API(API):

    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'

    param_zero ={
        'text': 'python',
        'per_page': 100,
        'area': 47,
        'data': 14
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_zero)
        pass

    def get_vacancies(self):
        response = requests.get(self.HH_API_URL, self.param)
        return response.json()["items"]
    def change_date(self):
        pass

    def add_word(self):
        pass

    def add_area(self):
        pass

    def load_all_areas(self):
        response = requests.get(self.HH_API_URL_AREAS)
        return response.json()




