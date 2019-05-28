from abc import ABC, abstractmethod

class IGeoRaster(ABC):
    """
    Esta interfaz las deben cumplir todos aquellas clases que representen objetos
    que estén compuestos por una rejila de coordenadas georeferenciada
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