from abc import ABC, abstractmethod


class IGeoRaster(ABC):
    """
    Esta interfaz la deben cumplir todas aquellas clases que representen objetos
    que estén compuestos por una rejilla de coordenadas georeferenciada
    """

    @property
    @abstractmethod
    def LAT(self):
        pass

    @property
    @abstractmethod
    def LON(self):
        pass

    @property
    @abstractmethod
    def X(self):
        pass

    @property
    @abstractmethod
    def Y(self):
        pass
