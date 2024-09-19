import streamlit as st
from assistant.task_manager import create_tasks_table, add_task, view_tasks, delete_task

# Ensure the table exists
create_tasks_table()

st.title("AI Personal Assistant")

# Add task
task = st.text_input("Enter a task:")
if st.button("Add Task"):
    add_task(task)
    st.success(f"Task '{task}' added.")

# View tasks
st.header("Tasks List")
tasks = view_tasks()
for task in tasks:
    st.write(f"ID: {task[0]}, Task: {task[1]}")

# Delete task
task_id = st.text_input("Enter Task ID to delete:")
if st.button("Delete Task"):
    delete_task(task_id)
    st.success(f"Task with ID {task_id} deleted.")
