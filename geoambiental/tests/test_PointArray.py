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

    def test_lon_min_lat_min(self):
        """
        Verifica que la propiedad lon_min y lat_min funcionen como deberían
        """
        self.assertAlmostEqual(self.p.lon_min, -118.25)
        self.assertAlmostEqual(self.p.lat_min, 20.23)

    def test_lon_max_lat_max(self):
        """
        Verifica que la propiedad lon_max y lat_max funcionen como deberían
        """
        self.assertAlmostEqual(self.p.lon_max, -110.25)
        self.assertAlmostEqual(self.p.lat_max, 23.05)

if __name__ == '__main__':
    unittest.main()
