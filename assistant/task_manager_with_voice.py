import sqlite3
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to create the tasks table if it doesn't exist
def create_tasks_table():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Create the 'tasks' table with scheduling fields
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  status TEXT NOT NULL DEFAULT 'pending',
                  due_date TEXT,
                  priority TEXT
                  )''')
    
    conn.commit()
    conn.close()

# Function to recreate the tasks table with updated schema
def recreate_tasks_table():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Create a new table with the correct schema
    c.execute('''
    CREATE TABLE IF NOT EXISTS new_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending',
        due_date TEXT,
        priority TEXT
    )
    ''')

    # Copy data from old table to new table, if it exists
    c.execute('''
    INSERT INTO new_tasks (id, task, status, due_date, priority)
    SELECT id, task, status, due_date, priority FROM tasks
    ''')
    
    # Drop the old table
    c.execute('DROP TABLE tasks')
    
    # Rename new table to old table name
    c.execute('ALTER TABLE new_tasks RENAME TO tasks')
    
    conn.commit()
    conn.close()

# Function to add a task with schedule (due date and priority)
def add_task_with_schedule(task, due_date, priority):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Insert a task with a due date and priority
    c.execute('INSERT INTO tasks (task, due_date, priority) VALUES (?, ?, ?)', (task, due_date, priority))
    
    conn.commit()
    conn.close()
    speak_text(f"Task '{task}' added with due date {due_date} and priority {priority}.")

# Function to view all tasks
def view_tasks():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Fetch all tasks
    c.execute('SELECT id, task FROM tasks')
    tasks = c.fetchall()
    
    conn.close()
    
    return tasks

# Function to view tasks with their schedule (due date and priority)
def view_scheduled_tasks():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Fetch tasks with due date and priority
    c.execute('SELECT id, task, due_date, priority, status FROM tasks')
    tasks = c.fetchall()
    
    conn.close()
    
    return tasks

# Function to delete a task based on task ID
def delete_task(task_id):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Delete the task based on the task ID
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    
    conn.commit()
    conn.close()
    speak_text(f"Task with ID {task_id} deleted.")

# Function to mark a task as complete
def complete_task(task_id):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Update the task's status to 'completed'
    c.execute('UPDATE tasks SET status = ? WHERE id = ?', ('completed', task_id))
    
    conn.commit()
    conn.close()
    speak_text(f"Task with ID {task_id} marked as completed.")

# Voice recognition for capturing tasks and commands
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak_text("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            speak_text("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Error connecting to Google API.")
            speak_text("Error connecting to Google API.")
            return None

# Text-to-speech function
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Ensure to recreate the tasks table with the new schema
recreate_tasks_table()
