"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import math 
import pytest
from src.calculator import add, divide, subtract, multiply, mul, div, power,square_root

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            mul("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            mul(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            div("10", 2)

def test_power_function():
    # positive powers
    assert power(2, 3) == 8
    assert power(5, 0) == 1

    # negative powers
    assert power(2, -2) == 0.25
    assert power(-2, 3) == -8

    # power of 1
    assert power(10, 1) == 10


def test_square_root_function():
    # perfect squares
    assert square_root(4) == 2
    assert square_root(16) == 4

    # non-perfect square
    assert round(square_root(2), 5) == 1.41421

    # zero
    assert square_root(0) == 0
