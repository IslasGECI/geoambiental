import unittest
import json

import numpy as np

from .. import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.p = Point(23.05, -118.25)

    def test_utm_coordinate(self):
        """
        Prueba que la coordenada se transforme a UTM de forma correcta
        """
        self.assertAlmostEqual(self.p.x, 371938.22957668)
        self.assertAlmostEqual(self.p.y, 2549601.77459413)

    def test_utm_zone(self):
        """
        Verifica que la salida de la propiedad utm_zone sea una lista donde el
        primer parámetro corresponda al número de la zona y el segundo a la letra
        """
        self.assertEqual(self.p.utm_zone[0], "11")
        self.assertEqual(self.p.utm_zone[1], "Q")

    
if __name__ == '__main__':
    unittest.main()
