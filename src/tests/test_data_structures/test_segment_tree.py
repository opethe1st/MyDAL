import os
import random
import unittest
from functools import reduce

from mydal.data_structures import SegmentTree


class SegmentTreeTestCase(unittest.TestCase):
    pass


class TestRangeQueryExceptions(SegmentTreeTestCase):

    def test_begin_greater_than_end(self):
        self.segmentTree = SegmentTree(arr=[1], func=None)
        with self.assertRaises(Exception) as exception_context:
            self.segmentTree.range_query(begin=1, end=0)
        self.assertEqual('begin cannot be greater than end', exception_context.exception.msg)

    def test_begin_end_invalid(self):
        self.segmentTree = SegmentTree(arr=[1], func=None)
        with self.assertRaises(Exception) as exception_context:
            begin = -1
            end = 1
            self.segmentTree.range_query(begin=begin, end=end)
        self.assertEqual('begin:{begin}, end:{end} out of bounds'.format(begin=begin, end=end), exception_context.exception.msg)

class TestSegmentTreeProduct(SegmentTreeTestCase):

    def test_range_10(self):
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.segmentTree = SegmentTree(arr=self.arr, func=lambda x, y: x*y)
        inputExpectedOutput = {
            (3, 7): 3*4*5*6*7,
            (1, 6): 1*2*3*4*5*6,
            (3, 4): 3*4,
            (3, 3): 3,
            (2, 2): 2,
            (4, 4): 4,
            (9, 9): 9,
            (8, 9): 72,
            (4, 9): 4*5*6*7*8*9
        }
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutput.items()):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.segmentTree.range_query(begin=inp[0], end=inp[1]))

    def test_range_generated_test(self):
        self.arr = list(range(20))
        self.segmentTree = SegmentTree(arr=self.arr, func=lambda x, y: x*y)
        inputExpectedOutputDict = {
        }
        testDataLocation = os.path.join(os.path.dirname(__file__), 'test_data.txt')
        with open(testDataLocation) as f:
            for line in f.readlines():
                in1, in2, out = list(map(int, line.split()))
                inputExpectedOutputDict[(in1, in2)] = out
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutputDict.items()):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.segmentTree.range_query(begin=inp[0], end=inp[1]))

class TestSegmentTreeAddition(SegmentTreeTestCase):

    def test_range_10(self):
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.segmentTree = SegmentTree(arr=self.arr, func=lambda x, y: x+y)
        inputExpectedOutput = {
            (3, 7): 3+4+5+6+7,
            (1, 6): 1+2+3+4+5+6,
            (3, 4): 3+4,
            (3, 3): 3,
            (2, 2): 2,
            (4, 4): 4,
            (9, 9): 9,
            (8, 9): 8+9,
            (0, 1): 1,
        }
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutput.items()):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.segmentTree.range_query(begin=inp[0], end=inp[1]))


class TestSegmentTreeMax(SegmentTreeTestCase):

    def test_range_10(self):
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.segmentTree = SegmentTree(arr=self.arr, func=max)
        inputExpectedOutput = {
            (3, 7): 7,
            (1, 6): 6,
            (3, 4): 4,
            (3, 3): 3,
            (2, 2): 2,
            (4, 4): 4,
            (9, 9): 9,
            (8, 9): 9,
        }
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutput.items()):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.segmentTree.range_query(begin=inp[0], end=inp[1]))


class TestSegmentTreeMin(SegmentTreeTestCase):

    pass

    def test_range_generated_test(self):
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.segmentTree = SegmentTree(arr=self.arr, func=min)
        inputExpectedOutputDict = {
            (0, 9): 0,
            (2, 3): 2,
            (5, 9): 5
        }
        for i, (inp, expectedOutput) in enumerate(inputExpectedOutputDict.items()):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput, self.segmentTree.range_query(begin=inp[0], end=inp[1]))
