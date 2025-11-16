# https://github.com/anishpat26-commits/lab10-AP-JJ.git
# Partner 1: Anish Patel
# Partner 2: James Jiang
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be not be 1 or less than or equal to zero..")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than zero.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b



