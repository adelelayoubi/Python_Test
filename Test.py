# this is a test

# hh
print("hello world!")
# math_functions.py

def add(a, b):
    """Addiert zwei Zahlen."""
    return a + b+1

def subtract(a, b):
    """Subtrahiert b von a."""
    return a - b

def multiply(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

def divide(a, b):
    """Dividiert a durch b. Wirft einen Fehler, wenn b gegen 0 geht."""
    if b == 0:
        raise ValueError("Teilung durch Null ist mathematisch nicht erlaubt!")
    return a / b
