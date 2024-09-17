import unittest
import sqlite3
from assistant.task_manager import add_task, view_tasks

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Set up a test database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE tasks (id INTEGER PRIMARY KEY, task TEXT)''')
        self.conn.commit()

    def tearDown(self):
        # Close the connection after tests
        self.conn.close()

    def test_add_task(self):
        # Add task and check that it is added to the database
        add_task("Complete project")
        
        # Fetch from the database to check if it's there
        self.cursor.execute('SELECT task FROM tasks')
        tasks = self.cursor.fetchall()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][0], "Complete project")

    def test_view_tasks(self):
        # Insert test data into the database
        self.cursor.execute('INSERT INTO tasks (task) VALUES (?)', ("Test Task",))
        self.conn.commit()

        # Call view_tasks to retrieve the tasks
        tasks = view_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test Task")

if __name__ == '__main__':
    unittest.main()
