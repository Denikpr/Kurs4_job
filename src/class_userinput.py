from src.classes_api import HeadHunterAPI, SuperJobAPI
from src.class_mylist import Mylist
from src.class_vacancy import Vacancy
import copy


class Userinput:
    """
    This class is for user interaction in console.
    """
    new_param = {
            'website': [],
            'city': [],
            'words': [],
            'date': 14
        }

    def __init__(self):
        self.hh_api = HeadHunterAPI()
        self.sj_api = SuperJobAPI()
        self.all_list = Mylist()
        self.mylist = Mylist()
        self.param = copy.deepcopy(self.new_param)

    def __call__(self):
        """
        First menu fo user.
        :return: None
        """
        while True:
            print('Выберите нужный пункт:')
            print('1 - Поиск вакансий')

            if self.mylist.vacancy_list != []:
                print('2 - Show favorite vacancies')

            print('0 - Выход')
            user_input = input()

            if user_input == '0':
                quit()
            elif user_input == '1':
                self.choosing_parameters()
            elif user_input == '2':
                print(self.mylist)
            else:
                print('Неизвестная команда')

    def choosing_parameters(self):
        """
        Second menu for choosing research's parameters
        :return: None
        """
        while True:
            self.delete_duplicates()
            print('Вы должны выбрать сайт, город,дату публикации,и слово для поиска')
            print(f'Мы ищем вакансии за последние {self.param["date"]} дней')
            if self.param['website'] != []:
                print(f"Вы выбрали сайт - {', '.join(self.param['website'])}")
            if self.param['city'] != []:
                print(f"Вы выбрали город - {', '.join(self.param['city'])}")
            if self.param['words'] != []:
                print(f"Вы ввели следующие слова для поиска- {', '.join(self.param['words'])}")
            print('1 - Выбрать сайт')
            print('2 - Добавить слово для поиска')
            print('3 - Выбрать город')
            print('4 - Изменить дату публикации (по умолчанию, 14 дней)')
            if self.param['website'] != [] and self.param['city'] != [] and self.param['words'] != []:
                print('5 - Поиск вакансии')
            print('0 - Выход')
            user_input = input()

            if user_input == '0':
                self.__call__()
            elif user_input == '1':
                self.choosing_website()
            elif user_input == '2':
                self.choosing_words()
            elif user_input == '3':
                self.choosing_city()
            elif user_input == '4':
                self.choosing_date()
            elif user_input == '5':
                self.research_vacancies()
            else:
                print('неизвестная команда')

    def choosing_website(self):
        """
        Menu for choosing websites
        :return: None
        """
        while True:
            print('Вы можете выполнить поиск на  HeadHunter и SuperJob. какой сайт Вы хотите выбрать?')
            print('1 - HeadHunter')
            print('2 - SuperJob')
            print('3 - HeadHunter и SuperJob')
            print('0 - Выход')
            user_input = input()

            if user_input == '0':
                break
            elif user_input == '1':
                self.param['website'].append('HeadHunter')
                break
            elif user_input == '2':
                self.param['website'].append('SuperJob')
                break
            elif user_input == '3':
                self.param['website'].append('HeadHunter')
                self.param['website'].append('SuperJob')
                break
            else:
                print('Неизвестная команда')

    def choosing_words(self):
        """
        Menu for add and delete word for researching
        :return: None
        """
        while True:
            self.delete_duplicates()
            if self.param['words'] != []:
                print(f"Вы ввели следующие слова - {', '.join(self.param['words'])}")
            print('Добавить слова для поиска или введите "удалить" все слова или выберите "0" для Выхода')
            user_input = input().lower()
            if user_input == '0':
                break
            elif user_input == 'удалить':
                self.param['words'].clear()
                break
            else:
                self.param['words'].append(user_input)
                break

    def choosing_city(self):
        """
        Adding city for researching
        :return: None
        """
        print('Добавьте город для поиска или нажмите 0 для выхода')
        while True:
            user_input = input().lower()
            if user_input == '0':
                break
            if self.check_city(user_input):
                self.param['city'].append(user_input)
                break
            else:
                print('Повторите снова. Так как мы не нашли этот город или нажали "0" для выхода')

    def check_city(self, user_input:str):
        """
        Checking city from user
        :param user_input: str
        :return: True or False
        """
        if self.hh_api.saver_areas.open_and_find_info(user_input) or self.sj_api.saver_areas.open_and_find_info(user_input):
            return True
        else:
            return False

    def choosing_date(self):
        """
        Choosing number of days for researching
        :return:
        """
        while True:
            print('Выберите количество дней для поиска')
            print('1 - 1 день')
            print('2 - 7 дней')
            print('3 - 14 дней')
            print('4 - 30 дней')
            print('0 - Выход')
            user_input = input()
            if user_input == '0':
                break
            elif user_input == '1':
                self.param['date'] = 1
                break
            elif user_input == '2':
                self.param['date'] = 7
                break
            elif user_input == '3':
                self.param['date'] = 14
                break
            elif user_input == '4':
                self.param['date'] = 30
                break
            else:
                print('Неизвестная команда')

    def research_vacancies(self):
        """
        Getting vacancies from HH and SJ, creating objects class Vacancy.
        :return: None
        """
        if 'HeadHunter' in self.param['website']:
            if self.param['city'] != []:
                for item in range(len(self.param['city'])):
                    self.hh_api.add_area(self.param['city'][item])
            if self.param['words'] != []:
                self.hh_api.add_words(self.param['words'])
            self.hh_api.change_date(self.param['date'])

            vacancies_hh = self.hh_api.get_vacancies()

            if vacancies_hh != []:
                for item in vacancies_hh:
                   vacancy = Vacancy.create_vacancy_from_hh(item)
                   self.all_list.add_vacancy(vacancy)

        if 'SuperJob' in self.param['website']:
            if self.param['city'] != []:
                for item in range(len(self.param['city'])):
                    self.sj_api.add_area(self.param['city'][item])
            if self.param['words'] != []:
                self.sj_api.add_words(self.param['words'])
            self.sj_api.change_date(self.param['date'])

            vacancies_sj = self.sj_api.get_vacancies()

            if vacancies_sj != []:
                for item in vacancies_sj:
                   vacancy = Vacancy.create_vacancy_from_sj(item)
                   self.all_list.add_vacancy(vacancy)

        self.param = copy.deepcopy(self.new_param)

        self.sorting_vacancies()

    def sorting_vacancies(self):
        """
        Menu for sort and filter vacancies
        :return: None
        """
        while True:
            print(f'Мы нашли {len(self.all_list)} вакансии. Мы можем их отсортировать или отфильтровать. Выберите что надо сделать?')
            print('1 - Отсортировать вакансии по дате')
            print('2 - Отсортировать вакансии по зарплате')
            print('3 - Отфильтровать по слову')
            print('4 - Отфильтровать по зарплате')
            print('5 - Показать все вакансии')
            print('6 - Сохранить все вакансии в CSV-файл')
            print('7 - Сохранить все вакансии в XLSX-файл')
            print('8 - Показать вакансии и добавить в список избранных')
            print('0 - Выход')

            user_input = input()

            if user_input == '0':
                self.__call__()
            elif user_input == '1':
                self.all_list.sorting_vacancies_data()
                self.showing_all_list_vacancies()
            elif user_input == '2':
                self.all_list.sorting_vacancies_salary()
                self.showing_all_list_vacancies()
            elif user_input == '3':
                print('Выбрать слово использовать для фильтра?')
                word_filter = input().lower()
                self.all_list.filter_list_word(word_filter)
                self.showing_all_list_vacancies()
            elif user_input == '4':
                print('Выбрать зарплату для фильтра')
                while True:
                    salary = input()
                    if salary.isdigit():
                        self.all_list.filter_list_salary(int(salary))
                        self.showing_all_list_vacancies()
                        break
                    else:
                        print('Некорректная зарплата')
            elif user_input == '5':
                self.showing_all_list_vacancies()
            elif user_input == '6':
                path = self.all_list.save_csv()
                print(f'Ваши выбранные вакансии были сохранены в CSV-файл - {path}')
                self.__call__()
            elif user_input == '7':
                path = self.all_list.save_xlsx()
                print(f'Ваши выбранные вакансии были сохранены в XLSX-файл - {path}')
                self.__call__()
            elif user_input == '8':
                self.showing_all_list_vacancies()
                self.choosing_vacancies_in_my_list()
            else:
                print('Неизвестная команда')

    def showing_all_list_vacancies(self):
        """
        Showing all vacancies
        :return: None
        """
        print(self.all_list)

    def choosing_vacancies_in_my_list(self):
        """
        Choosing favorite vacancies. Adding in favorite list.
        :return:
        """
        while True:
            print('Какие вакансии вы выбераете? Напишите цифру (через пробел, например "1 2 3 4 5").  Вы можете написать "все", чтобы добавить все вакансии в список избранных.')
            numbers_vacancies = input().lower()
            if numbers_vacancies == '0':
                break
            elif numbers_vacancies == 'все':
                for vacancy in self.all_list.vacancy_list:
                    self.mylist.add_vacancy(vacancy)

                self.saving_my_list_vacancies()
            else:
                numbers = []

                numbers_str = numbers_vacancies.split()
                for number_str in numbers_str:
                    if number_str.isdigit():
                        numbers.append(int(number_str))
                if numbers == []:
                    print('Повторите попытку или введите "0" для выхода')
                    continue

                for number in numbers:
                    if self.all_list.get_vacancy(number-1):
                        self.mylist.add_vacancy(self.all_list.get_vacancy(number-1))

                self.saving_my_list_vacancies()

    def saving_my_list_vacancies(self):
        """
        Last menu for saving vacancies in CSV-file.
        :return: None
        """
        while True:
            print(f'Мы добавили {len(self.mylist)} вакансии. МЫ можем сохранить их или сделать новый поиск. Выбирете что сделать дальше?')
            print('1 - Сохранить избранные вакансии в CSV файл')
            print('2 - Сохранить избранные вакансии в XLSX файл')
            print('3 - Вывести избранные вакансии')
            print('4 - Новый поиск')
            print('0 - Выход')

            user_input = input()

            if user_input == '0':
                self.__call__()
            elif user_input == '1':
                path = self.mylist.save_csv()
                print(f'Ваши избранные вакансии были сохранены в CSV-файл - {path}')
                self.__call__()
            elif user_input == '2':
                path = self.mylist.save_xlsx()
                print(f'Ваши избранные вакансии были сохранены в XLSX-файл - {path}')
                self.__call__()
            elif user_input == '3':
                print(self.mylist)
            elif user_input == '4':
                self.choosing_parameters()
            else:
                print('Неизвестная команда')

    def delete_duplicates(self):
        """
        Function for deleting duplicates in parameters
        :return: None
        """
        self.param = {
            'website': list(set(self.param['website'])),
            'city': list(set(self.param['city'])),
            'words': list(set(self.param['words'])),
            'date': self.param['date']
        }
