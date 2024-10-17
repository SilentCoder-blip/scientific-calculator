import streamlit as st
import math

# Function to evaluate the expression
def evaluate_expression(expr):
    try:
        # Replace 'x' with '*' for multiplication
        expr = expr.replace('x', '*')
        # Evaluate the expression
        return eval(expr)
    except Exception as e:
        return "Error"

# Streamlit application
st.title("Calculator")

# Input field for the user to enter expressions
expression = st.text_input("Enter your expression:")

# Button to calculate the result
if st.button("Calculate"):
    if expression:
        result = evaluate_expression(expression)
        st.write(f"Result: {result}")
    else:
        st.write("Please enter an expression.")

# Clear button
if st.button("Clear"):
    st.experimental_rerun()
