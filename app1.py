import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Function to perform calculations
def calculate_expression(expression):
    try:
        result = sp.sympify(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Function to plot graphs
# Updated plot function to handle vectorization properly
def plot_function(expression, x_range=(-10, 10)):
    try:
        x = sp.symbols('x')
        func = sp.sympify(expression)
        f_lambdified = sp.lambdify(x, func, modules=['numpy'])

        # Generate x values and corresponding y values
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        
        # Try to vectorize the function
        try:
            y_vals = f_lambdified(x_vals)
        except TypeError:
            # If the function can't handle vectorized input, calculate each value separately
            y_vals = np.array([f_lambdified(val) for val in x_vals])

        # Plotting
        plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label=f'y = {expression}', color='blue', linewidth=2)
        plt.title(f'Graph of {expression}', fontsize=16, color='red')
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


# Streamlit App Doraemon Themed UI
st.set_page_config(page_title="Doraemon Themed Calculator", page_icon="🧳", layout="centered")

# Custom Doraemon CSS
st.markdown("""
    <style>
        body {
            background-color: #E0F7FA; /* Doraemon blue background */
            color: #263238; /* Text color */
        }
        h1, h2, h3, label {
            color: #0277BD; /* Doraemon blue text */
        }
        h1 {
            text-align: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .doraemon-header {
            background-color: #0288D1;
            color: white;
            padding: 15px;
            border-radius: 10px;
        }
        .themed-button {
            background-color: #D32F2F; /* Doraemon red */
            color: white;
            font-size: 1.1rem;
            padding: 10px;
            width: 100%;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .themed-button:hover {
            background-color: #C62828;
        }
    </style>
    """, unsafe_allow_html=True)

# Doraemon Header
st.markdown("<h1 class='doraemon-header'>🧳 Doraemon Scientific Calculator</h1>", unsafe_allow_html=True)

# Doraemon image at the top (use a link to an online image)
st.image("https://upload.wikimedia.org/wikipedia/en/b/bd/Doraemon_character.png", width=200)

# Input for math expression
st.subheader("Enter a mathematical expression (e.g., 2*x + 3, sin(x), exp(x)):")
user_input = st.text_input("Expression", value="sin(x)", help="Enter expressions like sin(x), log(x), exp(x)")

# Calculate button with custom style
if st.button("🧮 Calculate", key="calculate"):
    result = calculate_expression(user_input)
    st.success(f"Result: {result}")

# Graph section with dynamic sliders
st.subheader("Plot the graph of the function:")
x_min = st.slider("X-axis minimum value", -20, 0, value=-10)
x_max = st.slider("X-axis maximum value", 0, 20, value=10)

# Plot graph button
if st.button("📈 Plot Graph", key="plot"):
    plot_function(user_input, x_range=(x_min, x_max))

# Fun message at the bottom
st.markdown("## Thanks for using Doraemon's Calculator! 😊")

