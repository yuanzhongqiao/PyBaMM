#
# Tests for the Unary Operator classes
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import pybamm

import unittest


def test_function(arg):
    return arg + arg


class TestUnaryOperators(unittest.TestCase):
    def test_unary_operator(self):
        a = pybamm.Symbol("a", domain=["test"])
        un = pybamm.UnaryOperator("unary test", a)
        self.assertEqual(un.children[0].name, a.name)
        self.assertEqual(un.domain, a.domain)

    def test_negation(self):
        a = pybamm.Symbol("a")
        nega = pybamm.Negate(a)
        self.assertEqual(nega.name, "-")
        self.assertEqual(nega.children[0].name, a.name)

        b = pybamm.Scalar(4)
        negb = pybamm.Negate(b)
        self.assertEqual(negb.evaluate(), -4)

    def test_absolute(self):
        a = pybamm.Symbol("a")
        absa = pybamm.AbsoluteValue(a)
        self.assertEqual(absa.name, "abs")
        self.assertEqual(absa.children[0].name, a.name)

        b = pybamm.Scalar(-4)
        absb = pybamm.AbsoluteValue(b)
        self.assertEqual(absb.evaluate(), 4)

    def test_function(self):
        a = pybamm.Symbol("a")
        funca = pybamm.Function(a, test_function)
        self.assertEqual(funca.name, "test_function")
        self.assertEqual(funca.children[0].name, a.name)

        b = pybamm.Scalar(123)
        funcb = pybamm.Function(b, test_function)
        self.assertEqual(funcb.evaluate(), 246)

    def test_gradient(self):
        a = pybamm.Symbol("a")
        grad = pybamm.Gradient(a)
        self.assertEqual(grad.children[0].name, a.name)

    def test_printing(self):
        a = pybamm.Symbol("a")
        self.assertEqual(str(-a), "-a")
        grad = pybamm.Gradient(a)
        self.assertEqual(grad.name, "grad")
        self.assertEqual(str(grad), "grad(a)")

    def test_id(self):
        a = pybamm.Scalar(4)
        un1 = pybamm.UnaryOperator("test", a)
        un2 = pybamm.UnaryOperator("test", a)
        un3 = pybamm.UnaryOperator("new test", a)
        self.assertEqual(un1.id, un2.id)
        self.assertNotEqual(un1.id, un3.id)
        a = pybamm.Scalar(4)
        un4 = pybamm.UnaryOperator("test", a)
        self.assertEqual(un1.id, un4.id)
        d = pybamm.Scalar(42)
        un5 = pybamm.UnaryOperator("test", d)
        self.assertNotEqual(un1.id, un5.id)


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()
