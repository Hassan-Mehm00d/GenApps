import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define a function to perform calculations
def calculate_expression(expression):
    try:
        # Evaluate the expression
        result = sp.sympify(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Define a function to plot graphs
def plot_function(expression, x_range=(-10, 10)):
    try:
        x = sp.symbols('x')
        func = sp.sympify(expression)
        f_lambdified = sp.lambdify(x, func, modules=['numpy'])

        # Generate x values and corresponding y values
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        y_vals = f_lambdified(x_vals)

        # Plotting the function
        plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label=f'y = {expression}', color='blue', linewidth=2)
        plt.title(f'Graph of {expression}', fontsize=16, color='darkblue')
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        st.pyplot(plt)
        plt.close()
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Streamlit App UI with Modern Layout
st.set_page_config(page_title="Modern Scientific Calculator", page_icon="🔢", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 10px;
        }
        h1 {
            color: darkblue;
            text-align: center;
            font-size: 3rem;
        }
        label {
            font-size: 1.1rem;
            color: darkblue;
        }
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🔢 Modern Scientific Calculator")

# Input section
st.subheader("Enter a mathematical expression (e.g., 2*x + 3, sin(x), exp(x))")

# User input for mathematical expression
user_input = st.text_input("Expression", value="sin(x)", help="You can enter expressions like sin(x), log(x), exp(x), etc.")

# Dropdown to select popular functions
st.subheader("Choose common functions:")
function_choice = st.selectbox("Choose a function", ["None", "sin(x)", "cos(x)", "tan(x)", "log(x)", "exp(x)"])
if function_choice != "None":
    user_input = function_choice

# Calculate result
if st.button("Calculate"):
    result = calculate_expression(user_input)
    st.success(f"Result: {result}")

# Graph section
st.subheader("Plot the graph of the function")

# Range for X-axis using sliders
x_min = st.slider("X-axis minimum value", -20, 0, value=-10)
x_max = st.slider("X-axis maximum value", 0, 20, value=10)

# Plot the graph dynamically
if st.button("Plot Graph"):
    plot_function(user_input, x_range=(x_min, x_max))

# Add an extra visual element
st.markdown("## 🎨 Modern Look for Interactive Calculator")
st.info("This calculator supports complex math expressions with dynamic graph plotting for visual analysis!")

