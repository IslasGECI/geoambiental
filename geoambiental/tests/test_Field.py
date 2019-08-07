from datetime import datetime
import unittest
import json

import numpy as np

from .. import Field


class TestGrid(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.fechas = [datetime(2018, 11, 1), datetime(2018, 11, 2)]
        self.field = Field([23.05, 22.05], [-118.25, -117.22], np.array([[[5, 4], [7, 8]], [[8, 9], [10, 11]]]), self.fechas, "lat,lon,t")


    def test_date(self):
        self.assertEqual(self.field.date, self.fechas)

    def test_getitem(self):
        self.assertTrue(self.field[0][0], 5)

if __name__ == '__main__':
    unittest.main()
