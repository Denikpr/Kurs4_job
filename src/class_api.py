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
        'per_page': 5,
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
    SJ_TOKEN = 'v3.r.11439952.6468e5f8ea084a2b1a2c5b94398a1114d7e032d9.5288be6ffde188c194b264bf4fb844a89e8a5365'

    param_zero ={
        'keyword': 'python',
        'count': 5,
        'town': 47,
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_zero)
        pass

    def get_vacancies(self):
        headers = {
            'X-Api-App-Id': self.SJ_TOKEN
        }
        response = requests.get(self.SJ_API_URL, headers=headers, params=self.param)
        return response.json()

    def change_date(self):
        pass

    def add_word(self):
        pass

    def add_area(self):
        pass

    def load_all_areas(self):
        response = requests.get(self.SJ_API_URL_AREAS)
        return response.json()




