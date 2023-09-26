from src.class_userinput import UserInput
from src.class_api import HeadHunter_API,SuperJob_API
from pprint import pprint

if __name__ == '__main__':
    #userinput = UserInput()
    #userinput()
    #hh_api = HeadHunter_API()
    ##data = hh_api.get_vacancies()
    ##pprint(data, indent=2)
    #areas = hh_api.load_all_areas()
    #pprint(areas, indent=2)
    sj_api = SuperJob_API()
    data = sj_api.get_vacancies()
    pprint(data, indent=2)
    print(len(sj_api.get_vacancies()))
    #areas = sj_api.load_all_areas()
    #pprint(areas, indent=2)


