import sqlite3

# Function to create the tasks table if it doesn't exist
def create_tasks_table():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Create the 'tasks' table
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  status TEXT NOT NULL DEFAULT 'pending'
                  )''')
    
    conn.commit()
    conn.close()

# Function to add a task
def add_task(task):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Insert a new task into the tasks table
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    
    conn.commit()
    conn.close()

# Function to view all tasks
def view_tasks():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Fetch all tasks
    c.execute('SELECT id, task FROM tasks')
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
