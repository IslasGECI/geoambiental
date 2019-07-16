from __future__ import annotations

from matplotlib import path
import numpy as np

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
        return self._area()

    @property
    def perimetro_km(self) -> float:
        return self.length_km

    @property
    def perimetro_m(self) -> float:
        return self.length_m

    @property
    def punto_medio(self) -> Point:
        return Point(self.lat.mean(), self.lon.mean())

    def _area(self) -> float:
        # https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
        return 0.5*np.abs(np.dot(self.x, np.roll(self.y, 1))-np.dot(self.y, np.roll(self.x, 1)))

    def in_polygon(self, geo_reference: IGeoReference):
        es_dentro = []
        poligono = path.Path([coordenada for coordenada in zip(self.lon,self.lat)])
        for lon, lat in zip(geo_reference.lon, geo_reference.lat):
            es_dentro.append(poligono.contains_points([(lon, lat)])[0])
        return es_dentro
