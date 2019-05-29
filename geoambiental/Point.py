import numpy as np
import utm

from . import IGeoReference


class Point(IGeoReference):
    """
    Clase que representa un punto georeferenciado en el espacio.

    Parámetros
    ----------
    `lat : float`
        Coordenada norte

    `lon : float`
        Coordenada este

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
    Crear un punto
    >>> p = geoambiental.Point(23.05, -118.25)
    >>> p.x
    array(371938.22957668)
    """

    def __init__(self, lat: float, lon: float):
        self._lat = lat
        self._lon = lon

    @property
    def lat(self) -> np.array:
        return np.array(self._lat)

    @property
    def lon(self) -> np.array:
        return np.array(self._lon)

    @property
    def x(self) -> np.array:
        x, _, _, _ = utm.from_latlon(self._lat, self._lon)
        return np.array(x)

    @property
    def y(self) -> np.array:
        _, y, _, _ = utm.from_latlon(self._lat, self._lon)
        return np.array(y)

    @property
    def utm_zone(self) -> str:
        _, _, zona, letra = utm.from_latlon(self._lat, self._lon)
        return np.array([zona, letra])
