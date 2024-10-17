import streamlit as st
import math

# Title of the web app
st.title("Scientific Calculator")

# Add more scientific operations to the dropdown menu
operations = ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Exponentiation", "Sine", "Cosine", "Tangent", "Logarithm"]
operation = st.selectbox("Choose an operation", operations)

# Inputs for numbers (some operations may require only one input)
if operation == "Square Root" or operation in ["Sine", "Cosine", "Tangent", "Logarithm"]:
    num1 = st.number_input("Enter a number:", value=0.0)
    num2 = None
else:
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)

# Function definitions for basic and scientific operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def exponentiation(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x)

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Square Root":
        result = square_root(num1)
    elif operation == "Exponentiation":
        result = exponentiation(num1, num2)
    elif operation == "Sine":
        result = sine(num1)
    elif operation == "Cosine":
        result = cosine(num1)
    elif operation == "Tangent":
        result = tangent(num1)
    elif operation == "Logarithm":
        result = logarithm(num1)
    
    st.write(f"The result is: {result}")
