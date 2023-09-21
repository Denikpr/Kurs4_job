from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass


class HeadHunter_API(API):
    pass


class SuperJob_API(API):
    pass




