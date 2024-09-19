import sqlite3

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('data/tasks.db', check_same_thread=False)
c = conn.cursor()

# Create the tasks table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
''')

conn.commit()

def add_task(task):
    """Add a new task to the SQLite database."""
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()

def view_tasks():
    """Retrieve all tasks from the SQLite database."""
    c.execute('SELECT id, task FROM tasks')
    tasks = c.fetchall()
    return tasks

def delete_task(task_id):
    """Delete a task from the SQLite database by task ID."""
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
