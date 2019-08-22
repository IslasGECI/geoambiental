import json
import unittest

import numpy as np

from .. import Grid


class TestGrid(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.grid = Grid([23.05, 22.05], [-118.25, -117.22])

    def test_LON_LAT_shape(self):
        """
        Verifica que el grid tenga las dimensiones correctas
        """
        self.assertTrue(self.grid.LON.shape, (2, 2))
        self.assertTrue(self.grid.LAT.shape, (2, 2))

    def test_X_Y_shape(self):
        """
        Verifica que el grid tenga las dimensiones correctas
        """
        self.assertTrue(self.grid.X.shape, (2, 2))
        self.assertTrue(self.grid.Y.shape, (2, 2))

    def test_lon_lat(self):
        """
        Verifica que las coordenadas sean correctas
        """
        self.assertTrue(np.array_equal(self.grid.lon, [-118.25, -117.22]))
        self.assertTrue(np.array_equal(self.grid.lat, [23.05, 22.05]))

    def test_x_y_shape(self):
        """
        Verifica que las coordenadas tengan las dimensiones correctas
        """
        self.assertTrue(self.grid.x.shape, (2,))
        self.assertTrue(self.grid.y.shape, (2,))

    def test_utm_zone_shape(self):
        """
        Verifica que la zona utm tenga las dimensiones correctas
        """
        self.assertTrue(self.grid.utm_zone.shape, (2, 2))


if __name__ == '__main__':
    unittest.main()
