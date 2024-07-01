import streamlit as st
import functions
st.title("Todo App")
st.text("This is my app")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              key="new_todo", on_change=add_todo)

