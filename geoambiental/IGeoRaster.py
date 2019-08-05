from abc import ABC, abstractmethod

class IGeoRaster(ABC):
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