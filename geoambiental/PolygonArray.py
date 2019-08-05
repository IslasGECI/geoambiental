from __future__ import annotations

from typing import List

import numpy as np
import utm

from .IGeoReference import IGeoReference
from .Point import Point
from . import Polygon

# Documentación de los tipos de retorno
FloatArray = List[float]
StringArray = List[str]

class PolygonArray(IGeoReference):
    """
    Clase que representa un arreglo de geoambiental.Polygon. Este objeto se
    puede producir cuando se importan datos desde un gpx, kml o un archivo shp.

    Parámetros
    ----------
    `PolygonArray : list`
        Lista que contiene un arreglo de geoambiental.Polygon.
    
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

    `x_min : float`
        Coordenada más al oeste del conjunto de polígonos.

    `x_max : float`
        Coordenada más al este del conjunto de polígonos.

    `y_min : float`
        Coordenada más al sur del conjunto de polígonos.

    `y_max : float`
        Coordenada más al norte del conjuntode polígonos.

    `lon_min : float`
        Coordenada más al oeste del conjunto de polígonos.

    `lon_max : float`
        Coordenada más al este del conjunto de polígonos.

    `lat_min : float`
        Coordenada más al sur del conjunto de polígonos.

    `lat_max : float`
        Coordenada más al norte del conjunto de polígonos.

    `utm_zone : List[str]`
        Arreglo con las zonas utm de las coordenadas de todos los polígonos
        separados por un nan.

    
    Métodos
    -------
    `in_polygon(polygon: geoambiental.Polygon): PolygonArray`
        Regresa un geoambiental.PolygonArray que contiene los polígonos
        contenidos **completamente** dentro del polígono que se pasa como
        argumento.
    
    Notas
    -----
    None
    
    Ejemplos
    --------
    Se puede obtener un geoambiental.PolygonArray desde un archivo shp:
    >>> linea_costa_guadalupe = geoambiental.io.import_coast_line("guadalupe_LCosta.shp", projection="epsg:4484")
    Para graficar la línea de costa se puede utilizar
    >>> plt.fill(puntos_madrigueras.lon, puntos_madrigueras.lat, "#FFFAE6", edgecolor="k", linewidth=.5)
    Para obtener solo el primer polígono del arreglo:
    >>> primer_islote = linea_costa_guadalupe[0] # se obtiene un geoambiental.Polygon
    """
    def __init__(self, PolygonArray: list):
        self._polygons = PolygonArray

    def __getitem__(self, index) -> PointArray:
        return self._polygons[index]

    @property
    def polygons(self) -> PointArray:
        return self._polygons

    @property
    def lon(self) -> FloatArray:
        return np.concatenate([np.concatenate([poligono.lon, [np.nan]]) for poligono in self._polygons])

    @property
    def lat(self) -> FloatArray:
        return np.concatenate([np.concatenate([poligono.lat, [np.nan]]) for poligono in self._polygons])

    @property
    def x(self) -> FloatArray:
        return np.concatenate([np.concatenate([poligono.x, [np.nan]]) for poligono in self._polygons])

    @property
    def y(self) -> FloatArray:
        return np.concatenate([np.concatenate([poligono.y, [np.nan]]) for poligono in self._polygons])

    @property
    def utm_zone(self) -> StringArray:
        return np.concatenate([np.concatenate([poligono.utm_zone, [np.nan]]) for poligono in self._polygons])

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

    def in_polygon(self, polygon: Polygon) -> PolygonArray:
        # TODO: Implementar método para extraer los polígonos que se encuentran
        # contenidos en el polígono que se pasó al método
        raise NotImplementedError
