from __future__ import annotations

from typing import List

import numpy as np
import utm

from . import IGeoReference
from . import IGeoReferenceFinite
from . import Point
from . import PointArray
from . import distance_between_points_m

# Documentación de los tipos de retorno
FloatArray = List[float]
StringArray = List[str]

class Line(IGeoReference, IGeoReferenceFinite):
    def __init__(self, lat, lon):
        self._lon = lon
        self._lat = lat

    @staticmethod
    def from_point_array(point_array) -> Line:
        puntos = PointArray([], [])
        puntos._puntos = point_array
        return Line(puntos.lat, puntos.lon)

    def __getitem__(self, index) -> Line:
        return Line(self.lat[index], self.lon[index])

    def to_point_array(self) -> PointArray:
        return PointArray(self._lat, self._lon)

    @property
    def lon(self) -> FloatArray:
        return np.array(self._lon)

    @property
    def lat(self) -> FloatArray:
        return np.array(self._lat)

    @property
    def x(self) -> FloatArray:
        x = [[utm.from_latlon(lat, lon)[0]] for lat, lon in zip(self._lat, self._lon)]
        return np.column_stack(x)[0]

    @property
    def y(self) -> FloatArray:
        y = [[utm.from_latlon(lat, lon)[1]] for lat, lon in zip(self._lat, self._lon)]         
        return np.column_stack(y)[0]

    @property
    def utm_zone(self) -> StringArray:
        zona = np.array([utm.from_latlon(lat, lon)[2:] for lat, lon in zip(self._lat, self._lon)])
        return zona

    @property
    def x_min(self) -> float:
        return self.x.min()

    @property
    def x_max(self) -> float:
        return self.x.max()

    @property
    def y_min(self) -> float:
        return self.y.min()

    @property
    def y_max(self) -> float:
        return self.y.max()

    @property
    def lat_min(self) -> float:
        return self.lat.min()

    @property
    def lat_max(self) -> float:
        return self.lat.max()

    @property
    def lon_min(self) -> float:
        return self.lon.min()

    @property
    def lon_max(self) -> float:
        return self.lon.max()

    @property
    def length_m(self):
        distancia = 0
        for i, (lat, lon) in enumerate(zip(self.lat, self.lon)):
            if i == len(self.lon) -1: break
            distancia += distance_between_points_m(Point(lat, lon), Point(self.lat[i+1], self.lon[i+1]))
        return distancia

    @property
    def length_km(self):
        return self.length_m / 1_000
