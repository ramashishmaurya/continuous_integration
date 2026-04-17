import streamlit as st

st.title("Power Calculator")

# User input (age or any number)
num = st.number_input("Enter your age or number:", value=1)

# Calculations
square = num ** 2
cube = num ** 3
power_5 = num ** 5

# Display results
st.write("### Results")
st.write(f"Square (x²): {square}")
st.write(f"Cube (x³): {cube}")
st.write(f"Power 5 (x⁵): {power_5}")