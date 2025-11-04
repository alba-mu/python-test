import pytest

def division(a,b):
   return a / b

def test_int_division():
   assert division(6,3) == 2
   assert division(9,3) == 3

def test_float_division():
   assert division(5, 2) == 2.5
   assert division(2, 3)

def test_with_alphabetic_strings():
    with pytest.raises(TypeError):
        division('a', 3)

def test_with_numeric_strings():
    with pytest.raises(TypeError):
        division('6', 3)

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(2,0)