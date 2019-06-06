from __future__ import annotations

from typing import List

import numpy as np
import utm

from . import IGeoReference
from . import IGeoReferenceFinite
from .Point import Point

# Documentación de los tipos de retorno
FloatArray = List[float]
StringArray = List[str]

class PointArray(IGeoReference, IGeoReferenceFinite):
    def __init__(self, lat, lon):
        self._create_points(lat, lon)

    @staticmethod
    def from_point_array(point_array) -> PointArray:
        puntos = PointArray([], [])
        puntos._puntos = point_array
        return puntos

    def _create_points(self, lat, lon):
        self._puntos = []
        latitudes = np.array(lat)
        longitudes = np.array(lon)
        for lat, lon in zip(latitudes, longitudes):
            self._puntos.append(Point(lat, lon))
        self._puntos = np.array(self._puntos)

    def __getitem__(self, index) -> PointArray:
        return PointArray.from_point_array(self._puntos[index])

    @property
    def points(self) -> PointArray:
        return self._puntos

    @property
    def lon(self) -> FloatArray:
        return np.array([punto.lon for punto in self._puntos])

    @property
    def lat(self) -> FloatArray:
        return np.array([punto.lat for punto in self._puntos])

    @property
    def x(self) -> FloatArray:
        return np.array([punto.x for punto in self._puntos])

    @property
    def y(self) -> FloatArray:
        return np.array([punto.y for punto in self._puntos])

    @property
    def utm_zone(self) -> StringArray:
        return np.array([punto.utm_zone for punto in self._puntos])

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

