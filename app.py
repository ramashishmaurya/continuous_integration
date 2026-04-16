import streamlit as st 

st.title('Power Calculator')
st.write('Enter the number')

n = st.number_input('Enter the Integers' ,step=1 ,value=1)

square = n**2 
cube = n**3
fitth_power = n**5

st.write(f'the square number {n} is :{square}')

st.write(f'the cube  number {n} is :{cube}')
st.write(f'the square number {n} is :{fitth_power}')