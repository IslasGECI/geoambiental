from abc import ABC, abstractmethod


class IGeoReference(ABC):
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
