from math_operation import add, subtract, multiply

import pytest 


@pytest.mark.parametrize(
    "a,b, expected", [(2,3,5), (-1,1,0)])

def test_add(a,b, expected):
    assert add(a,b) == expected
    
def test_subtract():
    assert subtract(3,2) == 1

def test_multiply():    
    assert multiply(2,3)  == 6