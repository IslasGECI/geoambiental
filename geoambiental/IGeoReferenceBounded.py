from abc import ABC, abstractmethod
from .IGeoReference import IGeoReference

from .Point import Point


class IGeoReferenceBounded(ABC):
    @property
    @abstractmethod
    def area_ha(self) -> float:
        pass

    @property
    @abstractmethod
    def area_km2(self) -> float:
        pass

    @property
    @abstractmethod
    def area_m2(self) -> float:
        pass

    @property
    @abstractmethod
    def perimetro_km(self) -> float:
        pass

    @property
    @abstractmethod
    def perimetro_m(self) -> float:
        pass

    @property
    @abstractmethod
    def punto_medio(self) -> Point:
        pass

    @abstractmethod
    def in_polygon(self, geo_reference: IGeoReference) -> bool:
        pass
