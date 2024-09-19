import streamlit as st
from assistant.voice_assistant import recognize_speech, speak_text
from assistant.task_manager import add_task, view_tasks, delete_task
from assistant.scheduler import schedule_task
from datetime import datetime

import sys
import os

# Ensure the assistant folder is in the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'assistant'))

from assistant.voice_assistant import recognize_speech, speak_text

st.title("AI Personal Assistant")

# Add task manually
task = st.text_input("Enter a task:")
if st.button("Add Task"):
    add_task(task)
    st.success(f"Task '{task}' added.")

# Schedule task reminder
reminder_time = st.text_input("Enter reminder time (YYYY-MM-DD HH:MM:SS):")
if st.button("Schedule Task"):
    try:
        reminder_datetime = datetime.strptime(reminder_time, '%Y-%m-%d %H:%M:%S')
        schedule_task(task, reminder_datetime)
        st.success(f"Task '{task}' scheduled for {reminder_time}")
    except ValueError:
        st.error("Invalid date/time format!")

# View tasks
st.header("Tasks List")
tasks = view_tasks()
for t in tasks:
    st.write(f"ID: {t[0]}, Task: {t[1]}, Created at: {t[2]}")

# Delete task
task_id = st.number_input("Enter Task ID to delete:", min_value=1, step=1)
if st.button("Delete Task"):
    delete_task(task_id)
    st.success(f"Task with ID {task_id} deleted.")

# Voice recognition
if st.button("Use Voice Assistant"):
    text = recognize_speech()
    st.write(f"You said: {text}")
    speak_text("You said " + text)
