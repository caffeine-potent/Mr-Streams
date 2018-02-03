import mr_streams as ms
import unittest
from operator import add

# :::: auxilary functions ::::
def add_one(x):
    return x + 1
def repeat_n_times(x, n = 1):
    return [x] * n
def double(x):
    return [x,x]

class TestMisc(unittest.TestCase):
    def test_001(self):
        _ = ms.stream([1,2,3,4,5])
        _ = _.map(add,1)\
                .map(add_one)\
                .flatmap( double)\
                .flatmap(repeat_n_times,  n = 2)
        _.drain()
