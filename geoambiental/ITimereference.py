from abc import ABC, abstractmethod


class ITimereference(ABC):
    @property
    @abstractmethod
    def date(self):
        pass
