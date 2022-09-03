import unittest
import sys
import os
sys.path.append(os.path.abspath("../RLWE/"))
from ring_element import RingElement
from numpy.polynomial import Polynomial


class TestRingElement(unittest.TestCase):

    def setUp(self):
        self.m = 2**2
        self.q = 10

    def test_modulo_number(self):
        r1 = RingElement(Polynomial([11, 12]), self.m, self.q)
        r2 = RingElement(Polynomial([1, 2,0]), self.m, self.q)
        self.assertEqual(r1, r2)

    def test_modulo_phi(self):
        poly = Polynomial([1, 2, 3])
        r1 = RingElement(poly, self.m, self.q)
        r2 = RingElement(poly + 5 * r1.get_cyclotomic(), self.m, self.q)
        self.assertTrue(r1 == r2)

    def test_add(self):
        r1 = RingElement(Polynomial([2, 3]), self.m, self.q)
        r2 = RingElement(Polynomial([1, 2]), self.m, self.q)
        expected = RingElement(Polynomial([3, 5]), self.m, self.q)
        self.assertTrue(expected == r1 + r2)

    def test_sub(self):
        r1 = RingElement(Polynomial([2, 3]), self.m, self.q)
        r2 = RingElement(Polynomial([1, 2]), self.m, self.q)
        expected = RingElement(Polynomial([1, 1]), self.m, self.q)
        self.assertTrue(expected == r1 - r2)

    def test_multi(self):
        # (2+3x)(1+2x)=2 + 7x + 6x^2
        # (6 + 7x) + (x^2 + 1)6
        r1 = RingElement(Polynomial([2, 3]), self.m, self.q)
        r2 = RingElement(Polynomial([1, 2]), self.m, self.q)
        expected = RingElement(Polynomial([6, 7]), self.m, self.q)
        self.assertTrue(expected == r1 * r2)

    def test_change_modulo(self):
        r1 = RingElement(Polynomial([2, 3]), self.m, self.q)
        result = r1.change_modulo(2)
        expected = RingElement(Polynomial([0, 1]), self.m, 2)
        self.assertEqual(expected, result)

    def test_compose(self):
        r = RingElement(Polynomial([15, 123, 7, 99]), 8, 256)
        x_power_3 = Polynomial([0, 0, 0, 1])
        result = r.compose(x_power_3)
        expected = RingElement(Polynomial([15, 99, 249, 123]), 8, 256)
        self.assertEqual(expected, result)
