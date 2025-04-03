def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    assert fahrenheit > -459.67
    return multiply(subtract(fahrenheit, 32), 5.0 / 9.0) # <-- Fix this in step 7
