import logging
import math

class CustomException(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

# log = logging.getLogger()

class SegmentTree:

    def __init__(self, arr, func):
        self._arr = arr
        self._m = [-1]*(2**int(math.log2(len(arr))+1)*2)
        self._func = func
        self._initialize(index=1, begin=0, end=len(self._arr)-1)

    def _initialize(self, index, begin, end):
        if begin == end:
            self._m[index] = self._arr[begin]
        else:
            self._initialize(index=2*index, begin=begin, end=(begin+end)//2)
            self._initialize(index=2*index+1, begin=(begin+end)//2+1, end=end)
            self._m[index] = self._func(self._m[index*2], self._m[index*2+1])

    def range_query(self, begin, end):
        if begin > end:
            raise CustomException(msg='begin cannot be greater than end')
        if begin < 0 or end > (len(self._arr)-1):
            raise CustomException(msg='begin:{begin}, end:{end} out of bounds'.format(begin=begin, end=end))
        return self._search(index=1, leftBound=0, rightBound=len(self._arr)-1, begin=begin, end=end)

    def _search(self, index, leftBound, rightBound, begin, end):
        # log.info('...', index, leftBound, rightBound, begin, end)
        # print('...', index, leftBound, rightBound, begin, end)
        mid = (leftBound+rightBound)//2
        if leftBound == begin and rightBound == end:
            return self._m[index]
        elif leftBound <= begin <= end <= mid:
            # print(1)
            return self._search(index=2*index, leftBound=leftBound, rightBound=mid, begin=begin, end=end)
        elif mid+1 <= begin <= end <= rightBound:
            # print(2)
            return self._search(index=2*index+1, leftBound=mid+1, rightBound=rightBound, begin=begin, end=end)
        elif leftBound <= begin <= end <= rightBound:
            # print(3)
            return self._func(
                self._search(index=2*index, leftBound=leftBound, rightBound=mid, begin=begin, end=mid), 
                self._search(index=2*index+1, leftBound=mid+1, rightBound=rightBound, begin=mid+1, end=end)
            )
        else:
            pass # pragma: no cover
            # log.error('...shouldnt get here', index, leftBound, rightBound, begin, end)
            # print('...shouldnt get here', leftBound, rightBound, begin, end)
