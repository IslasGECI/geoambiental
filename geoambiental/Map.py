import numpy as np
import utm

from .Grid import Grid
from .interfaces import IGeoReferenceBounded
from .Point import Point


class Map(Grid):
    def __init__(self, lat, lon, value):
        super(Map, self).__init__(lat, lon)
        self._value = value

    @property
    def value(self):
        return self._value

    def set_nan_outside(self, geo_reference_bounded: IGeoReferenceBounded):
        LON = np.full(self.LON.shape, np.nan)
        LAT = np.full(self.LAT.shape, np.nan)
        variables = np.full(self.value.shape, np.nan)
        for i, lat in enumerate(self.lat):
            for j, lon in enumerate(self.lon):
                es_dentro = geo_reference_bounded.in_polygon(
                    Point([self.LAT[i][j]], [self.LON[i][j]]))
                if es_dentro[0]:
                    LON[i][j] = self.LON[i][j]
                    LAT[i][j] = self.LAT[i][j]
                    variables[i][j] = self.value[i][j]
        return Map(LAT, LON, variables)
