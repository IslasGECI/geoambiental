import unittest
import json

import numpy as np

from .. import Point
from .. import Polygon


class TestPolygon(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.p = Polygon([23.05, 20.23, 19.20], [-118.25, -110.25, -110.3])

    def test_utm_coordinate(self):
        """
        Verifica que la coordenada se transforme a UTM de forma correcta
        """        
        self.assertTrue(np.allclose(self.p.x, [371938.22957668, 578341.05641097, 573587.90026725]))
        self.assertTrue(np.allclose(self.p.y, [2549601.77459413, 2237110.74773384, 2123105.08841421]))

    def test_lon_lat_numpy(self):
        """
        Verifica que las coordenadas sean un arreglo de numpy
        """
        self.assertTrue(isinstance(self.p.lon, np.ndarray))

    def test_utm_zone(self):
        """
        Verifica que la salida de la propiedad utm_zone sea una lista de listas
        donde el primer parámetro corresponda al número de la zona y el segundo
        a la letra
        """        
        self.assertEqual(self.p.utm_zone[0][0], "11")
        self.assertEqual(self.p.utm_zone[0][1], "Q")
        self.assertEqual(self.p.utm_zone[1][0], "12")
        self.assertEqual(self.p.utm_zone[1][1], "Q")

    def test_lon_min_lat_min(self):
        """
        Verifica que la propiedad lon_min y lat_min funcionen como deberían
        """
        self.assertAlmostEqual(self.p.lon_min, -118.25)
        self.assertAlmostEqual(self.p.lat_min, 19.20)

    def test_lon_max_lat_max(self):
        """
        Verifica que la propiedad lon_max y lat_max funcionen como deberían
        """
        self.assertAlmostEqual(self.p.lon_max, -110.25)
        self.assertAlmostEqual(self.p.lat_max, 23.05)

    def test_from_point_array(self):
        """
        Verifica que se pueda crear un polígono de puntos desde una lista de
        objetos Point
        """
        punto_1 = Point(23.05, -118.25)
        punto_2 = Point(20.23, -110.25)
        punto_3 = Point(19.20, -110.3)
        arreglo_puntos = Polygon.from_point_array([punto_1, punto_2, punto_3])
        self.assertTrue(np.allclose(self.p.x, arreglo_puntos.x))

    def test_in_polygon(self):
        """
        Verifica que el método in_polygon funcione correctamente
        """
        poligono = Polygon([23, 23, 24, 24], [-118, -119, -119, -118])
        punto = Point([23.5], [-118.5])
        self.assertTrue(poligono.in_polygon(punto)[0])

    def test_punto_medio(self):
        """
        Verifica que el punto medio se calcule de forma correcta
        """        
        self.assertAlmostEqual(self.p.punto_medio.lon, -112.93333, places=5)

    def test_area_m(self):
        """
        Verifica que el área se calcule de manera correcta
        """
        latitude_world = [-90, 90, 90, -90, -90]
        longitude_world = [-180, -180, 180, 180, -180]
        poligono = Polygon(latitude_world, longitude_world)
        self.assertAlmostEqual(poligono.area_m2, 511207893395811.06)

    def test_area_km(self):
        """
        Verifica que el área se calcule de manera correcta
        """
        latitude_world = [-90, 90, 90, -90, -90]
        longitude_world = [-180, -180, 180, 180, -180]
        poligono = Polygon(latitude_world, longitude_world)
        self.assertAlmostEqual(poligono.area_km2, 511207893395811.06*1e-6)

if __name__ == '__main__':
    unittest.main()
