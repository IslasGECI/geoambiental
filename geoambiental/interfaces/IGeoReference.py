from abc import ABC, abstractmethod


class IGeoReference(ABC):
    """
    Esta interfaz las deben cumplir todos aquellos objetos tengan coordenadas
    georeferenciada, no está pensada para rejillas de coordenadas
    """
    @property
    @abstractmethod
    def x(self) ->float:
        pass

    @property
    @abstractmethod
    def y(self) -> float:
        pass

    @property
    @abstractmethod
    def lon(self) -> float:
        pass

    @property
    @abstractmethod
    def lat(self) -> float:
        pass

    @property
    @abstractmethod
    def utm_zone(self) -> str:
        pass
