#coding=utf-8
from count import Count

class TestCount:
    def test_add(self):
        try:
            j = Count(2,3)
            add = j.add()
            assert (add==6),'cwls'
        except AssertionError as msg:
            print(msg)
        else:
            print('test pass')
mytest = TestCount()
mytest.test_add()