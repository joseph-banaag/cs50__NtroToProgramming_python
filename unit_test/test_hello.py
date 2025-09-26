from hello import hello

def test_argument():
    assert hello("David") == "Hello, David"

def test_default():
    assert hello() == "Hello, world!"





"""
NOTE:
    when creating a test function, use assert and test arguments 
for default and for the user input.
"""
