import sqlite3

# Database file path
DB_PATH = 'data/tasks.db'

def add_task(task):
    """Add a new task to the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Insert the task into the tasks table
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def view_tasks():
    """View all tasks stored in the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Retrieve all tasks from the tasks table
    c.execute('SELECT id, task, created_at FROM tasks')
    tasks = c.fetchall()
    
    conn.close()
    return tasks

def delete_task(task_id):
    """Delete a task from the database using its id."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Delete the task by its ID
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
