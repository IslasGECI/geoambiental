from abc import ABC, abstractmethod


class IGeoReferenceFinite(ABC):
    @property
    @abstractmethod
    def x_min(self) -> float:
        pass

    @property
    @abstractmethod
    def x_max(self) -> float:
        pass

    @property
    @abstractmethod
    def y_min(self) -> float:
        pass

    @property
    @abstractmethod
    def y_max(self) -> float:
        pass

    @property
    @abstractmethod
    def lon_min(self) -> float:
        pass

    @property
    @abstractmethod
    def lon_max(self) -> float:
        pass

    @property
    @abstractmethod
    def lat_min(self) -> float:
        pass

    @property
    @abstractmethod
    def lat_max(self) -> float:
        pass
