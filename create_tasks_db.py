import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('task_manager.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the 'tasks' table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  status TEXT NOT NULL
                  )''')

# Sample task data to insert into the table for testing
sample_task = ("Sample Task: Set up SQLite", "pending")

# Insert the sample task (this will create a new row in the 'tasks' table)
cursor.execute('INSERT INTO tasks (task, status) VALUES (?, ?)', sample_task)

# Commit the transaction to save the changes
conn.commit()

# Retrieve the inserted task to verify the connection
cursor.execute('SELECT * FROM tasks WHERE task = ?', (sample_task[0],))
task = cursor.fetchone()

# Output the inserted task
print(f"Inserted task: {task}")

# Close the connection
conn.close()

print("Database initialized and sample task inserted successfully.")
