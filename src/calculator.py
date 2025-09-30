"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""
import math 
def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

# TODO: Students will add multiply, divide, power, sqrt functions
def mul(a, b):
    """Simple multiplication with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def div(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ZeroDivisionError("Zero division! ERROR!") 
    return a / b

def power(base, exponent):
    return base ** exponent

def square_root(number):
    """Return square root, raise ValueError if negative input."""
    if number < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(number)

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")

    