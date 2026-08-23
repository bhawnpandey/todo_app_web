import streamlit as st
import functions 

st.title("My Todo App")
st.subheader("This is my todo app")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)


