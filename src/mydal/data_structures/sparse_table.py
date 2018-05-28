import math
from typing import List
from typing import Callable


class CustomException(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

class SparseTable:

    def __init__(self, arr: List, func: Callable[[int, int], int], start: int):
        self._arr = arr
        self._len = len(arr)
        self._func = func
        self._start = start
        self._m = self._initialize()

    def _initialize(self):
        depth = int(math.log2(self._len) + 1)
        m = [[float('inf') for i in range(self._len)] for j in range(depth)]

        m[0] = self._arr
        for depth in range(depth-1):
            index = 0
            step = 1 << (depth)
            while index+step < self._len:
                m[depth+1][index] = self._func(m[depth][index], m[depth][index+step])
                index += 1
        return m

    def range_query(self, begin, end):
        if end - begin < 0:
            raise CustomException(msg='begin has to be greater than end')
        if not(0 <= begin < self._len and 0 <= end < self._len):
            raise CustomException(msg='making a query beyond the bounds: begin - {begin}, end - {end}'.format(begin=begin, end=end))
        interval = end - begin + 1 
        depths = []
        depth = 0
        while interval > 0:
            if interval % 2 == 1:
                depths.append(depth)
            depth += 1
            interval //= 2
        ans = self._start
        index = begin
        for depth in depths:
            ans = self._func(ans, self._m[depth][index])
            index += (1 << depth)
        return ans
