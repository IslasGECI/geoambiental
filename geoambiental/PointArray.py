from __future__ import annotations

from typing import List

import numpy as np
import utm

from . import IGeoReference, IGeoReferenceFinite
from .Point import Point

# Documentación de los tipos de retorno
FloatArray = List[float]
StringArray = List[str]


class PointArray(IGeoReference, IGeoReferenceFinite):
    """
    Clase que representa un arreglo de punto georeferenciado en el espacio. Esta
    clase es similar a Line, pero se diferencían en la forma de representar los
    datos de forma interna, Line es más eficiente.

    Parámetros
    ----------
    `lat : list`
        Lista de coordenada norte

    `lon : list`
        Lista de coordenada este

    Atributos
    ----------
    `x : np.array`
        Arreglo con las coordenadas este de todos los polígonos separados por
        un nan.

    `y : np.array`
        Arreglo con las coordenadas norte de todos los polígonos separados por
        un nan.

    `lon : np.array`
        Arreglo con las longitudes de todos los polígonos separados por un nan.

    `lat : np.array`
        Arreglo con las latitudes de todos los polígonos separados por un nan.

    `utm_zone : np.array`
        Arreglo con las zonas utm de las coordenadas de todos los polígonos
        separados por un nan.

    Métodos
    -------
    Ninguno

    Notas
    -----
    Ninguna

    Ejemplos
    --------
    Crear un arreglo de puntos
    >>> p = geoambiental.PointArray([23.05, 20.23], [-118.25, -110.25])
    >>> p.lon
    array(-118.25, -110.25)
    >>> p.lon_min
    -110.25
    """

    def __init__(self, lat, lon):
        self._create_points(lat, lon)

    @staticmethod
    def from_point_array(point_array: list) -> PointArray:
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
        return np.array(self._puntos)

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
