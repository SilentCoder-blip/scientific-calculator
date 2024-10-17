import streamlit as st
import math

# Define the functions
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = "Error"
    return result

# Create a Streamlit app
st.title("Scientific Calculator")

# Display input field
expression = st.text_input("Enter your expression:", "")

# Display buttons
if st.button("Evaluate"):
    result = evaluate_expression(expression)
    st.write(f"Result: {result}")

# Optional advanced mathematical functions
st.write("### Advanced Functions")

# Trigonometric functions
if st.button("sin(x)"):
    expression += "math.sin("
if st.button("cos(x)"):
    expression += "math.cos("
if st.button("tan(x)"):
    expression += "math.tan("
if st.button("log(x)"):
    expression += "math.log("
if st.button("sqrt(x)"):
    expression += "math.sqrt("

st.write(f"Updated expression: {expression}")
