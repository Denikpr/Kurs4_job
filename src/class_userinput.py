from src.class_api import HeadHunter_API, SuperJob_API
from src.class_mylist import MyList
import copy

class UserInput:
    pass
    param_zero = {}
    def __init__(self):
        self.hh_api = HeadHunter_API()
        self.sj_api = SuperJob_API()
        self.all_list = MyList()
        self.favorite_list = MyList()
        self.param = copy.deepcopy(self.param_zero)
        pass
