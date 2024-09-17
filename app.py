import streamlit as st
from assistant.task_manager import add_task, view_tasks, delete_task

# Streamlit UI for adding and viewing tasks
st.title("Task Manager")

# Add a new task
task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    add_task(task)
    st.success(f"Task '{task}' added.")

# View tasks
st.header("Current Tasks")
tasks = view_tasks()
for task in tasks:
    st.write(f"ID: {task[0]} | Task: {task[1]} | Created at: {task[2]}")

# Delete a task
task_id = st.number_input("Enter Task ID to delete:", min_value=1, step=1)
if st.button("Delete Task"):
    delete_task(task_id)
    st.success(f"Task with ID {task_id} deleted.")
