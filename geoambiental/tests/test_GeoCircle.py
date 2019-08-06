import unittest
import json

import numpy as np

from .. import GeoCircle
from .. import Point


class TestGeoCircle(unittest.TestCase):

    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.centro = Point(24, -118)
        self.radio = 1_500
        self.n_vertices = 1_000
        self.circle = GeoCircle(self.centro, radius_m=self.radio, n_vertices=self.n_vertices)

    def test_n_vertices(self):
        """
        Verifica que la cantidad de vetices coincida con la cantidad de coordenadas
        """
        self.assertTrue(len(self.circle.lon) == self.n_vertices)

    def test_punto_medio(self):
        """
        Verifica que el punto medio caiga cerca del punto que se usó para definir el centro del círculo
        """
        self.assertAlmostEqual(self.circle.punto_medio.lon, self.centro.lon, places=0)
        self.assertAlmostEqual(self.circle.punto_medio.lat, self.centro.lat, places=0)

    def test_area_m2(self):
        """
        Verifica que el área se calcule de manera correcta
        """
        # Se acepta un pequeño error que viene del cálculo numérico del área
        self.assertTrue(abs(self.circle.area_m2) - (self.radio**2)*np.pi <= (self.radio**2)*np.pi*.1)


if __name__ == '__main__':
    unittest.main()
