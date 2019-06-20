import unittest
import json

import numpy as np

from .. import Point
from .. import operations


class TestDistance(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.p1 = Point(23.05, -118.25)
        self.p2 = Point(22.05, -117.22)

    def test_distance_between_points_km(self):
        """
        Prueba que la distancia en km entre las coordenada sea la correcta
        """        
        self.assertAlmostEqual(operations.distance_between_points_km(self.p1, self.p2)[0], 153.205, places=3)

    def test_distance_between_points_m(self):
        """
        Prueba que la distancia en m entre las coordenada sea la correcta
        """        
        self.assertAlmostEqual(operations.distance_between_points_m(self.p1, self.p2)[0], 153_205, places=0)


if __name__ == '__main__':
    unittest.main()
