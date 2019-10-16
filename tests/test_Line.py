import json
import unittest

import numpy as np

from geoambiental.Line import Line
from geoambiental.Point import Point


class TestLine(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.line = Line([23.05, 22.05], [-118.25, -117.22])

    def test_utm_coordinate(self):
        """
        Verifica que la coordenada se transforme a UTM de forma correcta
        """
        self.assertTrue(np.allclose(
            self.line.x, [371938.22957668, 477299.34]))
        self.assertTrue(np.allclose(
            self.line.y, [2549601.77459413, 2438377.63]))

    def test_lon_lat_numpy(self):
        """
        Verifica que las coordenadas sean un arreglo de numpy
        """
        self.assertTrue(isinstance(self.line.lon, np.ndarray))

    def test_utm_zone(self):
        """
        Verifica que la salida de la propiedad utm_zone sea una lista de listas
        donde el primer parámetro corresponda al número de la zona y el segundo
        a la letra
        """
        print(self.line.utm_zone)
        self.assertEqual(self.line.utm_zone[0][0], "11")
        self.assertEqual(self.line.utm_zone[0][1], "Q")
        self.assertEqual(self.line.utm_zone[1][0], "11")
        self.assertEqual(self.line.utm_zone[1][1], "Q")

    def test_lon_min_lat_min(self):
        """
        Verifica que la propiedad lon_min y lat_min funcionen como deberían
        """
        self.assertAlmostEqual(self.line.lon_min, -118.25)
        self.assertAlmostEqual(self.line.lat_min, 22.05)

    def test_lon_max_lat_max(self):
        """
        Verifica que la propiedad lon_max y lat_max funcionen como deberían
        """
        self.assertAlmostEqual(self.line.lon_max, -117.22)
        self.assertAlmostEqual(self.line.lat_max, 23.05)

    def test_to_point_array(self):
        """
        Verifica que se pueda hacer un _slice_ de la propiedad points
        """
        self.assertTrue(isinstance(
            self.line.to_point_array().points[1:], np.ndarray))

    def test_lenght_km(self):
        """
        Verifica que la longitud de la línea sea la correcta
        """
        self.assertAlmostEqual(self.line.length_km, 153.25379, places=3)

    def test_lenght_m(self):
        """
        Verifica que la longitud de la línea sea la correcta
        """
        self.assertAlmostEqual(self.line.length_m, 153_253.7964, places=0)

    def test_from_point_array(self):
        """
        Verifica que se pueda crear un arreglo de puntos desde una lista de
        objetos Point
        """
        punto_1 = Point(23.05, -118.25)
        punto_2 = Point(22.05, -117.22)
        arreglo_puntos = Line.from_point_array([punto_1, punto_2])
        self.assertTrue(np.allclose(self.line.x, arreglo_puntos.x))


if __name__ == '__main__':
    unittest.main()
