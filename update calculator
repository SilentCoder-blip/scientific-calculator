import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Title for the app
st.title("Scientific Calculator with Graphing")

# User input for expression or multiple values
expression = st.text_input("Enter a mathematical expression or values (comma-separated for multiple values):")

# Evaluate expression function
def evaluate_expression(expr):
    try:
        result = eval(expr)
        return result
    except:
        return "Invalid expression"

# Plot graph function
def plot_graph(expr):
    try:
        x = sp.Symbol('x')
        sympy_expr = sp.sympify(expr)
        func = sp.lambdify(x, sympy_expr, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        plt.figure()
        plt.plot(x_vals, y_vals)
        plt.title(f'Graph of {expr}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        st.pyplot(plt)
    except Exception as e:
        st.error("Invalid expression for plotting")

# Handle multiple values for sum
def handle_multiple_values(expr):
    try:
        values = expr.split(',')
        values = [float(val.strip()) for val in values]
        return sum(values)
    except:
        return "Invalid input for multiple values"

# Display buttons for actions
if st.button("Evaluate Expression"):
    result = evaluate_expression(expression)
    st.write(f"Result: {result}")

if st.button("Plot Graph"):
    plot_graph(expression)

if st.button("Calculate Sum of Multiple Values"):
    result = handle_multiple_values(expression)
    st.write(f"Sum: {result}")

# Footer
st.write("Created with ❤️ using Streamlit")
