from abc import ABC, abstractmethod


class Saver(ABC):
    pass


class JSON(Saver):
    pass


class SCV(Saver):
    pass


class XLSX(Saver):
    pass
