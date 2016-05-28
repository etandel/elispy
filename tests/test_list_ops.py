import unittest

from elispy import cons, head, tail, EMPTY


class ConsTestCase(unittest.TestCase):
    def test_cons_to_empty(self):
        v = cons(23, EMPTY)
        self.assertIsInstance(v, list)
        self.assertEqual(v, [23])

    def test_cons_to_non_enmpty(self):
        v = cons(23, cons(27, EMPTY))
        self.assertIsInstance(v, list)
        self.assertEqual(v, [23, 27])


class HeadTestCase(unittest.TestCase):
    def test_head_of_empty(self):
        self.assertRaises(ValueError, head, EMPTY)

    def test_head_of_non_enmpty(self):
        self.assertEqual(head([23, 27, 42]), 23)


class TailTestCase(unittest.TestCase):
    def test_head_of_empty(self):
        self.assertRaises(ValueError, tail, EMPTY)

    def test_head_of_non_enmpty(self):
        v = tail([23, 27, 42])
        self.assertIsInstance(v, list)
        self.assertEqual(v, [27, 42])

