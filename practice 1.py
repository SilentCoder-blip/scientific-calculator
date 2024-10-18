import streamlit as st
import math

# Title of the calculator
st.title("Scientific Calculator")

# Dropdown menu for selecting the operation
operation = st.selectbox(
    "Choose an operation:",
    ("Add", "Subtract", "Multiply", "Divide", "Square Root", 
     "Exponentiation", "Sine", "Cosine", "Tangent", "Logarithm")
)

# Input fields for the numbers
if operation in ("Sine", "Cosine", "Tangent", "Square Root", "Logarithm"):
    num1 = st.number_input("Enter the number:")
else:
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:", 0.0)

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of addition is {result}")

    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of subtraction is {result}")

    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of multiplication is {result}")

    elif operation == "Divide":
        if num2 == 0:
            st.error("Error! Division by zero.")
        else:
            result = num1 / num2
            st.success(f"The result of division is {result}")

    elif operation == "Square Root":
        if num1 < 0:
            st.error("Error! Cannot take the square root of a negative number.")
        else:
            result = math.sqrt(num1)
            st.success(f"The square root of {num1} is {result}")

    elif operation == "Exponentiation":
        result = math.pow(num1, num2)
        st.success(f"The result of exponentiation is {result}")

    elif operation == "Sine":
        result = math.sin(math.radians(num1))
        st.success(f"The sine of {num1} degrees is {result}")

    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
        st.success(f"The cosine of {num1} degrees is {result}")

    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
        st.success(f"The tangent of {num1} degrees is {result}")

    elif operation == "Logarithm":
        if num1 <= 0:
            st.error("Error! Logarithm only defined for positive numbers.")
        else:
            result = math.log(num1)
            st.success(f"The logarithm of {num1} is {result}")
