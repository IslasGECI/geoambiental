from abc import ABC, abstractmethod
from .IGeoReference import IGeoReference


class IGeoReferenceBounded(ABC):
    """
    Esta interfaz las deben cumplir todas aquellas clases que representen objetos
    que estén compuestos por una rejilla de coordenadas georeferenciada
    """
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
    def punto_medio(self) -> IGeoReference:
        pass

    @abstractmethod
    def in_polygon(self, geo_reference: IGeoReference) -> bool:
        pass
