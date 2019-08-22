import numpy as np
import utm

from .Point import Point
from .Polygon import Polygon


class GeoCircle(Polygon):
    def __init__(self, point: Point, radius_m: float, n_vertices: int = 100):
        t = np.linspace(0, 2*np.pi, n_vertices)
        x = radius_m*np.cos(t) + point.x
        y = radius_m*np.sin(t) + point.y
        longitude = []
        latitude = []
        for coordenada_x, coordenada_y in zip(x, y):
            lat, lon = utm.to_latlon(
                coordenada_x, coordenada_y, 11, "R", strict=False)
            longitude.append(lon)
            latitude.append(lat)

        super(GeoCircle, self).__init__(latitude, longitude)
