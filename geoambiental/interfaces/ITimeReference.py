from abc import ABC, abstractmethod


class ITimeReference(ABC):
    """
    Esta interfaz la deben cumplir todas aquellas clases que representen objetos
    que tengan una referencia temporal
    """

    @property
    @abstractmethod
    def date(self):
        pass
