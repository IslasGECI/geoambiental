import unittest
import json

import numpy as np

from .. import PointArray


class TestPointArray(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.p = PointArray([23.05, 20.23], [-118.25, -110.25])

    def test_utm_coordinate(self):
        """
        Prueba que la coordenada se transforme a UTM de forma correcta
        """        
        self.assertTrue(np.allclose(self.p.x, [371938.22957668, 578341.05641097]))
        self.assertTrue(np.allclose(self.p.y, [2549601.77459413, 2237110.74773384]))

if __name__ == '__main__':
    unittest.main()
