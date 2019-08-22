import json
import unittest

import numpy as np

from .. import Polygon, PolygonArray


class TestPolygonArray(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        p1 = Polygon([23.05, 20.23, 19.20], [-118.25, -110.25, -110.3])
        p2 = Polygon([25.15, 28.30, 17.20], [-111.25, -115.25, -119.3])
        self.polygon_array = PolygonArray([p1, p2])

    def test_lon_min(self):
        self.assertEqual(self.polygon_array.lon_min, -119.3)

    def test_lat_min(self):
        self.assertEqual(self.polygon_array.lat_min, 17.20)

    def test_lon_max(self):
        self.assertEqual(self.polygon_array.lon_max, -110.25)

    def test_lat_max(self):
        self.assertEqual(self.polygon_array.lat_max, 28.30)

    def test_x_min(self):
        self.assertEqual(self.polygon_array.x_min, 255387.13401107586)

    def test_y_min(self):
        self.assertEqual(self.polygon_array.y_min, 1903132.6462591637)

    def test_x_max(self):
        self.assertEqual(self.polygon_array.x_max, 671600.3271908131)

    def test_y_max(self):
        self.assertEqual(self.polygon_array.y_max, 3131678.287325614)

    def test_getitem(self):
        self.assertTrue(self.polygon_array[0].lon[0] == -118.25)


if __name__ == '__main__':
    unittest.main()
