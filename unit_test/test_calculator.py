import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(-0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


""" NOTE:

*: when writing test function always use test_ as the function 
name

*: when testing code, make sure to create multiple functions to test 
so that pytest will run through all of them and find the bug in one 
go




"""