import unittest

from elispy import add, sub, gt, cons, EMPTY
from elispy.core import if_, interpret


class InterpretTestCase(unittest.TestCase):
    def test_interpret_literal(self):
        self.assertEqual(interpret(add), add)

    def test_interpret_flat_sexp(self):
        sexp = (add, 1, 2, 3)
        self.assertEqual(interpret(sexp), 6)

    def test_interpret_nested_sexp(self):
        sexp = (cons, 24, (cons, 27, EMPTY))
        self.assertEqual(interpret(sexp), [24, 27])

    def test_flat_if(self):
        sexp_true = (if_, True, 1, 2)
        sexp_false = (if_, False, 1, 2)

        self.assertEqual(interpret(sexp_true), 1)
        self.assertEqual(interpret(sexp_false), 2)

    def test_nested_if(self):
        sexp = (
            if_,
            (gt, (add, 3, 5), (sub, 6, 5)),
            (cons, 23, (cons, 27, EMPTY)),
            (EMPTY)
        )
        self.assertEqual(interpret(sexp), [23, 27])

