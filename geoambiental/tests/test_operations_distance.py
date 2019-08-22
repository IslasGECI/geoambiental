import json
import unittest

import numpy as np

from .. import Point, operations


class TestDistance(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.p1 = Point(23.05, -118.25)
        self.p2 = Point(22.05, -105.22)

    def test_distance_between_points_km(self):
        """
        Prueba que la distancia en km entre las coordenada sea la correcta
        """
        self.assertAlmostEqual(operations.distance_between_points_km(
            self.p1, self.p2), 1344.371, places=2)

    def test_distance_between_points_m(self):
        """
        Prueba que la distancia en m entre las coordenada sea la correcta
        """
        self.assertAlmostEqual(operations.distance_between_points_m(
            self.p1, self.p2), 1344371.939, places=0)


if __name__ == '__main__':
    unittest.main()
