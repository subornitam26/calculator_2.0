import streamlit as st

st.title("Simple Calculator.")

num1 = st.number_input("First number :")
num2 = st.number_input("Second number :")
operator = st.selectbox("Choose a operator:",["+","-","*","/"])
if st.button("Calculate"):
     if operator == "+":
        result = num1 + num2
     elif operator == "-":
        result = num1 - num2
     elif operator == "*":
        result = num1 * num2
     elif operator == "/":
         if num2 != 0:
            result = num1 / num2
         else:
            result = "Cannot divide by zero"
     st.success(f"Result: {result}")