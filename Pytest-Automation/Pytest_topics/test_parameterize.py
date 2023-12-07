import pytest
import math


@pytest.mark.parametrize('test_input',[10,20,30,40])
def test_param01(test_input):
    assert test_input > 25



@pytest.mark.parametrize('inp,out',[(2,4),(3,27),(4,256)])
def test_param02(inp,out):
    assert (inp ** inp) == out


data = [
    ([1,2,3],'prod',6),
    ([5,6,7],'sum',18)
]


@pytest.mark.parametrize("a,b,c",data)
def test_param03(a,b,c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c