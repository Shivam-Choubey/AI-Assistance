from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import threading

app = Flask(__name__)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_text(text):
    def run_speech():
        engine.say(text)
        engine.runAndWait()

    # Run speech in a separate thread
    thread = threading.Thread(target=run_speech)
    thread.start()

def create_tasks_table():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  status TEXT NOT NULL DEFAULT 'pending',
                  due_date TEXT,
                  priority TEXT
                  )''')
    conn.commit()
    conn.close()

def add_task_with_schedule(task, due_date, priority):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task, due_date, priority) VALUES (?, ?, ?)', (task, due_date, priority))
    conn.commit()
    conn.close()
    speak_text(f"Task '{task}' added with due date {due_date} and priority {priority}.")

def view_scheduled_tasks():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute('SELECT id, task, due_date, priority, status FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    speak_text(f"Task with ID {task_id} deleted.")

def complete_task(task_id):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET status = ? WHERE id = ?', ('completed', task_id))
    conn.commit()
    conn.close()
    speak_text(f"Task with ID {task_id} marked as completed.")

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

# Create tasks table if it doesn't exist
create_tasks_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add_task' in request.form:
            task = request.form['task']
            due_date = request.form.get('due_date')
            priority = request.form.get('priority')
            add_task_with_schedule(task, due_date, priority)
            return redirect(url_for('index'))
        elif 'delete_task' in request.form:
            task_id = request.form['task_id']
            delete_task(task_id)
            return redirect(url_for('index'))
        elif 'complete_task' in request.form:
            task_id = request.form['task_id']
            complete_task(task_id)
            return redirect(url_for('index'))
    
    tasks = view_scheduled_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    if request.method == 'POST':
        if 'add_task' in request.form:
            speak_text("Please say the task")
            task = recognize_speech()
            if task:
                due_date = request.form.get('due_date')
                priority = request.form.get('priority')
                add_task_with_schedule(task, due_date, priority)
            else:
                speak_text("No valid task recognized.")
            return redirect(url_for('index'))
        elif 'complete_task' in request.form:
            speak_text("Please say the task ID to complete")
            task_id = recognize_speech()
            if task_id and task_id.isdigit():
                complete_task(int(task_id))
            else:
                speak_text("Invalid Task ID.")
            return redirect(url_for('index'))
        elif 'delete_task' in request.form:
            speak_text("Please say the task ID to delete")
            task_id = recognize_speech()
            if task_id and task_id.isdigit():
                delete_task(int(task_id))
            else:
                speak_text("Invalid Task ID.")
            return redirect(url_for('index'))
    
    return render_template('voice.html')

if __name__ == '__main__':
    app.run(debug=True)
