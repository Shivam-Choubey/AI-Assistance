import sqlite3

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

# Function to add a task without scheduling details
def add_task(task):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Insert a new task into the tasks table without due date or priority
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    
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

# Function to view all tasks
def view_tasks():
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Fetch all tasks
    c.execute('SELECT id, task, status FROM tasks')
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

# Function to mark a task as complete
def complete_task(task_id):
    conn = sqlite3.connect('task_manager.db')
    c = conn.cursor()

    # Update the task's status to 'completed'
    c.execute('UPDATE tasks SET status = ? WHERE id = ?', ('completed', task_id))
    
    conn.commit()
    conn.close()
