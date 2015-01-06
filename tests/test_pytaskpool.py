# coding=utf-8

import unittest
from time import sleep
from random import randint

import pytaskpool as tp


depth = 19
process = 3

# each process sleep between 0 and 256 ms
max_time = 256
depth_range = range(depth)

# function that simulate a process that take random time
def functest(x, wait=1):
    if wait:
        sleep_time = randint(0, max_time) / 1000.
        sleep(sleep_time)
    return [x]


expected = [functest(x, 0) for x in depth_range]

class TestTP(unittest.TestCase):
    def setUp(self):
        self.results = []
        self.mypool = tp.TaskPool([], process)
        self.assertIsInstance(self.mypool, tp.TaskPool)
        pass

    def test_init(self):
        self.assertIsInstance(self.mypool, tp.TaskPool)

    def test_launch(self):
        for y in depth_range:
            self.mypool.launch(functest, y)

    def test_unsorted_results(self):
        for y in depth_range:
            self.mypool.launch(functest, y)

        for r in self.mypool.get_unsorted_results():
            self.results += r
            self.assertIn(r, expected)

        self.assertEqual(len(self.results), depth)

    def test_sorted_results(self):
        for y in depth_range:
            self.mypool.launch(functest, y)

        for r in self.mypool.get_sorted_results():
            self.results += [r]

        self.assertEqual(self.results, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)