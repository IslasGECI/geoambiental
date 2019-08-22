import json
import unittest

import numpy as np

from .. import Point, Polygon, operations


class TestInPolygon(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.p1 = Point([23.05], [-118.25])
        self.poligono = Polygon(
            [22.05, 22.05, 24.05, 24.05], [-119.22, -117.22, -117.22, -119.22])

    def test_in_polygon(self):
        """
        Prueba que la distancia en km entre las coordenada sea la correcta
        """
        self.assertTrue(operations.in_polygon(self.p1, self.poligono))


if __name__ == '__main__':
    unittest.main()
