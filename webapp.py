import streamlit as st
import functions
todos=functions.get_todos()
st.title("Your Todo App")
st.header("Welcome!")
st.subheader("Make your Day Productive!")
st.write("Get started!!")

for i in todos:
    st.checkbox(i)

st.text_input(label="",placeholder="Type in a Todo")