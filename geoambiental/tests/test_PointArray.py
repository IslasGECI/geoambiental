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

    def test_lon_lat_numpy(self):
        """
        Esta prueba verifica que las coordenadas sean un arreglo de numpy
        """
        self.assertTrue(isinstance(self.p.lon, np.ndarray))

    def test_utm_zone(self):
        """
        Verifica que la salida de la propiedad utm_zone sea una lista de listas
        donde el primer parámetro corresponda al número de la zona y el segundo
        a la letra
        """        
        self.assertEqual(self.p.utm_zone[0][0], "11")
        self.assertEqual(self.p.utm_zone[0][1], "Q")
        self.assertEqual(self.p.utm_zone[1][0], "12")
        self.assertEqual(self.p.utm_zone[1][1], "Q")

if __name__ == '__main__':
    unittest.main()
