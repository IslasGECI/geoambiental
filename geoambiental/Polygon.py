from __future__ import annotations

from geoarea import area
from matplotlib import path
import numpy as np

from . import distance_between_points_m
from . import IGeoReference
from . import IGeoReferenceBounded
from . import IGeoReferenceFinite
from .Line import Line
from .Point import Point


class Polygon(Line, IGeoReferenceBounded):

    def __init__(self, lat, lon):
        super().__init__(lat, lon)

    @property
    def area_ha(self) -> float:
        return self.area_m2 * 1e-4

    @property
    def area_km2(self) -> float:
        return self.area_m2 * 1e-6

    @property
    def area_m2(self) -> float:
        return area(np.concatenate([self.lat, self.lat[0].reshape(1,)]), np.concatenate([self.lon, self.lon[0].reshape(1,)]))

    @property
    def perimetro_km(self) -> float:
        return self.perimetro_m*1_000

    @property
    def perimetro_m(self) -> float:
        distancia = 0
        # Se agrega la distancia del último al primer vertice para que el polígono sea cerrado
        for i, (lat, lon) in enumerate(zip(np.concatenate([self.lat, self.lat[0].reshape(1,)]), np.concatenate([self.lon, self.lon[0].reshape(1,)]))):
            if i == len(self.lon) -1: break
            distancia += distance_between_points_m(Point(lat, lon), Point(self.lat[i+1], self.lon[i+1]))
        return distancia

    @property
    def punto_medio(self) -> Point:
        return Point(self.lat.mean(), self.lon.mean())

    def in_polygon(self, geo_reference: IGeoReference):
        es_dentro = []
        poligono = path.Path([coordenada for coordenada in zip(self.lon,self.lat)])
        for lon, lat in zip(geo_reference.lon, geo_reference.lat):
            es_dentro.append(poligono.contains_points([(lon, lat)])[0])
        return es_dentro
