import os
import unittest

from mydal.data_structures.sparse_table import SparseTable


class SparseTableTestCase(unittest.TestCase):
    pass


class TestExceptions(SparseTableTestCase):

    def setUp(self):
        self.arr = [1, 2, 3, 2, 1, 2, 10, 1, 2, 1]
        self.sparseTable = SparseTable(arr=self.arr, func=max, start=-float('inf'))

    def test_begin_greater_end(self):
        with self.assertRaises(Exception) as exception_context:
            self.sparseTable.range_query(begin=1, end=0)
        self.assertEqual('begin has to be greater than end', exception_context.exception.msg)

    def test_out_of_bounds(self):
        with self.assertRaises(Exception) as exception_context:
            begin = -1
            end = 0
            self.sparseTable.range_query(begin=begin, end=end)
        self.assertEqual(
            'making a query beyond the bounds: begin - {begin}, end - {end}'.format(begin=begin, end=end), 
            exception_context.exception.msg
        )


class TestMax(SparseTableTestCase):

    def setUp(self):
        self.arr = [1, 2, 3, 2, 1, 2, 10, 1, 2, 1]
        self.sparseTable = SparseTable(arr=self.arr, func=max, start=-float('inf'))

    def test_random(self):
        inputExpectedOutput = {
            (1, 3): 3, 
            (6, 6): 10, 
            (9, 9): 1
        }
        for inp, expectedOutput in inputExpectedOutput.items():
            with self.subTest():
                self.assertEqual(expectedOutput, self.sparseTable.range_query(begin=inp[0], end=inp[1]))


class TestProduct(SparseTableTestCase):

    def setUp(self):
        self.arr = [1, 2, 3, 2, 1, 2, 10, 1, 2, 1]
        self.sparseTable = SparseTable(arr=self.arr, func=lambda x, y: x*y, start=1)

    def test_random(self):
        inputExpectedOutput = {
            (1, 3): 12, 
            (6, 6): 10, 
            (9, 9): 1,
            (0, 5): 24, 
            (5, 6): 20
        }
        for inp, expectedOutput in inputExpectedOutput.items():
            with self.subTest():
                self.assertEqual(expectedOutput, self.sparseTable.range_query(begin=inp[0], end=inp[1]))

    def test_range_generated_test(self):
        self.arr = list(range(20))
        self.sparseTable = SparseTable(arr=self.arr, func=lambda x, y: x*y, start=1)
        # import pdb; pdb.set_trace()
        inputExpectedOutputDict = {
        }
        testDataLocation = os.path.join(os.path.dirname(__file__), 'test_data.txt')
        with open(testDataLocation) as f:
            for line in f.readlines():
                in1, in2, out = list(map(int, line.split()))
                inputExpectedOutputDict[(in1, in2)] = out
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutputDict.items()):
            # print(inp, expectedOutput, self.sparseTable.range_query(begin=inp[0], end=inp[1]))
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.sparseTable.range_query(begin=inp[0], end=inp[1]))

class TestMin(SparseTableTestCase):

    def setUp(self):
        self.arr = [1, 2, 3, 2, 1, 2, 10, 1, 2, 1, 100, -1, -3]
        self.sparseTable = SparseTable(arr=self.arr, func=min, start=float('inf'))

    def test_random(self):
        inputExpectedOutput = {
            (1, 3): 2, 
            (6, 6): 10, 
            (9, 9): 1, 
            (0, 9): 1, 
            (12, 12): -3
        }
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutput.items()):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.sparseTable.range_query(begin=inp[0], end=inp[1]))
