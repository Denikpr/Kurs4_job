from src.class_api import HeadHunter_API, SuperJob_API
from src.class_mylist import MyList

class UserInput:
    pass

    def __init__(self):
        self.hh_api = HeadHunter_API()
        self.sj_api = SuperJob_API()
        self.my_list = MyList()
    def __call__(self):
        pass
