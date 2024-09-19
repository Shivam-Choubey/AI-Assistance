import sqlite3
from datetime import datetime

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('data/tasks.db', check_same_thread=False)
c = conn.cursor()

# Create the tasks table if it doesn't exist, with 'created_at' timestamp
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()

def add_task(task):
    """Add a new task to the SQLite database with timestamp."""
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()

def view_tasks():
    """Retrieve all tasks from the SQLite database, including created_at timestamp."""
    c.execute('SELECT id, task, created_at FROM tasks')
    tasks = c.fetchall()
    return tasks

def delete_task(task_id):
    """Delete a task from the SQLite database by task ID."""
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
