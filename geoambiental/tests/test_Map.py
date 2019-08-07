import unittest
import json

import numpy as np

from .. import Map


class TestMap(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.map = Map([23.05, 22.05], [-118.25, -117.22], np.array([[5, 4], [7, 8]]))

    def test_value_shape(self):
        """
        Verifica que el grid tenga las dimensiones correctas
        """
        self.assertTrue(self.map.LON.shape == self.map.value.shape)


if __name__ == '__main__':
    unittest.main()
