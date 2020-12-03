import numpy as np
import utm

from .interfaces import IGeoRaster, IGeoReference, IGeoReferenceBounded
from .Point import Point


class Grid(IGeoRaster, IGeoReference):
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon

    @property
    def LAT(self) -> np.array:
        return np.meshgrid(self._lon, self._lat)[1]

    @property
    def LON(self) -> np.array:
        return np.meshgrid(self._lon, self._lat)[0]

    @property
    def Y(self):
        coor_y = np.zeros(self.LAT.shape)
        for i, lat in enumerate(self.LAT):
            for j, lon in enumerate(self.LON):
                _, y, _, _ = utm.from_latlon(self.LAT[i][j], self.LON[i][j])
                coor_y[i][j] = y
        return coor_y

    @property
    def X(self):
        coor_x = np.zeros(self.LON.shape)
        for i, lat in enumerate(self.LAT):
            for j, lon in enumerate(self.LON):
                x, _, _, _ = utm.from_latlon(self.LAT[i][j], self.LON[i][j])
                coor_x[i][j] = x
        return coor_x

    @property
    def lat(self):
        return np.array(self._lat)

    @property
    def lon(self):
        return np.array(self._lon)

    @property
    def y(self):
        return np.array(self.Y[:, 1])

    @property
    def x(self):
        return np.array(self.X[1, :])

    @property
    def utm_zone(self):
        zona_utm = np.empty(self.LON.shape, dtype=object)
        for i, lat in enumerate(self.lat):
            for j, lon in enumerate(self.lon):
                _, _, numero, letra = utm.from_latlon(self.LAT[i][j], self.LON[i][j])
                zona_utm[i][j] = str(numero) + letra
        return zona_utm

    def set_nan_outside(self, geo_reference_bounded: IGeoReferenceBounded):
        LON = np.full(self.LON.shape, np.nan)
        LAT = np.full(self.LAT.shape, np.nan)
        for i, lat in enumerate(self.lat):
            for j, lon in enumerate(self.lon):
                es_dentro = geo_reference_bounded.in_polygon(
                    Point([self.LAT[i][j]], [self.LON[i][j]])
                )
                if es_dentro[0]:
                    LON[i][j] = self.LON[i][j]
                    LAT[i][j] = self.LAT[i][j]
        return Grid(LAT, LON)
