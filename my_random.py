# my_random.py

import math
import random as py_random  # using Python's built-in random internally if needed

# Simple arithmetic function
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

# Multiply two numbers
def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

# Generate a random integer in a range
def random_int(start, end):
    """Return a random integer between start and end inclusive."""
    return py_random.randint(start, end)

# Calculate factorial
def factorial(n):
    """Return factorial of a number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Return a random choice from a list
def random_choice(seq):
    """Return a random element from a sequence."""
    if not seq:
        raise ValueError("Sequence is empty")
    return py_random.choice(seq)
