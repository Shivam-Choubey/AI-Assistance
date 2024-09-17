import sqlite3

def initialize_db():
    # Connect to the SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('data/tasks.db')
    c = conn.cursor()

    # Create the tasks table
    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
    print("Database and table initialized successfully.")
