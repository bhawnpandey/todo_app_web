import streamlit as st
import functions 

st.title("My Todo App")
st.subheader("This is my todo app")

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox_value = st.checkbox(todo, key=todo)
    if checkbox_value:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add a new todo", placeholder="Add new todo..", key="new_todo", on_change=add_todo, label_visibility="collapsed")





