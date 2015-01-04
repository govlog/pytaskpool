# coding=utf-8

import unittest

import pytaskpool as tp


class TestTP(unittest.TestCase):
    def setUp(self):

        self.result = []

        self.mypool = tp.TaskPool([], 2)

        self.expected = [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000, 285311670611,
                         8916100448256, 302875106592253, 11112006825558016, 437893890380859375]
        pass

    def test_tp_create(self):
        self.assertIsInstance(self.mypool, tp.TaskPool)

    def test_multi_process(self):

        def testfunc(x):
            return [x ** x]

        for y in range(16):
            self.mypool.launch(testfunc, y)

        for r in self.mypool.get_unsorted_results():
            self.assertIn(r[0], self.expected)

        for r in self.mypool.get_sorted_results():
            self.result += r

        self.assertEqual(self.result, self.expected)


if __name__ == '__main__':
    unittest.main()
