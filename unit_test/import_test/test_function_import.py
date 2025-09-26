from unit_test.calculator import square

def test_square():
    assert square(5) == 25

# using relative import works with testing using pytest
