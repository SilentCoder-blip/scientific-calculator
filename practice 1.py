import streamlit as st
import math

# Title of the web app
st.title("Scientific Calculator")

# Add more scientific operations to the dropdown menu
operations = ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Exponentiation", "Sine", "Cosine", "Tangent", "Logarithm"]
operation = st.selectbox("Choose an operation", operations)

# Dynamic number of inputs
st.write("Enter numbers (at least one):")

# Ask user how many inputs they want (min 1)
num_inputs = st.number_input("How many numbers do you want to input?", min_value=1, max_value=10, value=2)

# Collect input fields based on the number selected
numbers = []
for i in range(num_inputs):
    numbers.append(st.number_input(f"Enter number {i+1}:", value=0.0))

# Function definitions for basic and scientific operations
def add(nums):
    return sum(nums)

def subtract(nums):
    result = nums[0]
    for num in nums[1:]:
        result -= num
    return result

def multiply(nums):
    result = 1
    for num in nums:
        result *= num
    return result

def divide(nums):
    result = nums[0]
    for num in nums[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def exponentiation(base, exp):
    return math.pow(base, exp)

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
        result = add(numbers)
    elif operation == "Subtract":
        result = subtract(numbers)
    elif operation == "Multiply":
        result = multiply(numbers)
    elif operation == "Divide":
        result = divide(numbers)
    elif operation == "Square Root":
        if len(numbers) == 1:
            result = square_root(numbers[0])
        else:
            result = "Square root requires exactly 1 number."
    elif operation == "Exponentiation":
        if len(numbers) == 2:
            result = exponentiation(numbers[0], numbers[1])
        else:
            result = "Exponentiation requires exactly 2 numbers (base and exponent)."
    elif operation == "Sine":
        if len(numbers) == 1:
            result = sine(numbers[0])
        else:
            result = "Sine requires exactly 1 number (angle in degrees)."
    elif operation == "Cosine":
        if len(numbers) == 1:
            result = cosine(numbers[0])
        else:
            result = "Cosine requires exactly 1 number (angle in degrees)."
    elif operation == "Tangent":
        if len(numbers) == 1:
            result = tangent(numbers[0])
        else:
            result = "Tangent requires exactly 1 number (angle in degrees)."
    elif operation == "Logarithm":
        if len(numbers) == 1:
            result = logarithm(numbers[0])
        else:
            result = "Logarithm requires exactly 1 number (must be positive)."
    
    st.write(f"The result is: {result}")
