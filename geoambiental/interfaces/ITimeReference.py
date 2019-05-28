from abc import ABC, abstractmethod


class ITimeReference(ABC):
    @property
    @abstractmethod
    def date(self):
        pass
