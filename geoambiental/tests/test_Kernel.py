import unittest
import json

import numpy as np

from .. import PointArray
from .. import get_kernel_density_geographic, get_kernel_density


class TestKernel(unittest.TestCase):

    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.point_array = self.p = PointArray([23.05, 20.23], [-118.25, -110.25])

    def test_result_matrix_shape_square(self):
        self.assertTrue(get_kernel_density_geographic(self.point_array)[0].shape == (100,100))
        self.assertTrue(get_kernel_density(self.point_array)[0].shape == (100,100))


if __name__ == '__main__':
    unittest.main()
