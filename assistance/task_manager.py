import sqlite3

def add_task(task):
    conn = sqlite3.connect('data/tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('data/tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks
