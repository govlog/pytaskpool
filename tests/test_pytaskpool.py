# coding=utf-8

import unittest
import pytaskpool as tp

def testfunc(x):
    return [x ** x]

depth = 128
depth_range = range(depth)

expected = [testfunc(x) for x in depth_range]

class TestTP(unittest.TestCase):
    def setUp(self):
        self.results = []
        self.mypool = tp.TaskPool([],3)
        pass

    def test_init(self):
        self.assertIsInstance(self.mypool, tp.TaskPool)

    def test_launch(self):
        for y in depth_range:
            self.mypool.launch(testfunc, y)

    def test_unsorted_results(self):
        for y in depth_range:
            self.mypool.launch(testfunc, y)

        for r in self.mypool.get_unsorted_results():
            self.results += r
            self.assertIn(r, expected)

        self.assertEqual(len(self.results),depth)

    def test_sorted_results(self):
        for y in depth_range:
            self.mypool.launch(testfunc, y)

        for r in self.mypool.get_sorted_results():
            self.results += [r]

        self.assertEqual(self.results, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)