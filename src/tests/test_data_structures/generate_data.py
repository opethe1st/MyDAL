import random
from functools import reduce


if __name__ == '__main__':
    inputExpectedOutputDict = []
    for i in range(100000):
        a, b = random.randint(0, 19), random.randint(0, 19) 
        a, b = min(a, b), max(a, b)
        inputExpectedOutputDict.append((a, b, reduce(lambda x, y: x*y, range(a, b+1), 1)))

    with open('test_data.txt', 'w') as f:
        for inp1, inp2, out in inputExpectedOutputDict:
            f.write('{start} {end} {ans}\n'.format(start=inp1, end=inp2, ans=out))
