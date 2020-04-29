import unittest
import search


class ClassTests(unittest.TestCase):
    def test_01(self):
        result = search.method()
        self.assertEqual('Hello World!', result)
