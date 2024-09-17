import unittest
from unittest.mock import patch
from datetime import datetime
from assistant.scheduler import schedule_task

class TestScheduler(unittest.TestCase):

    @patch('assistant.scheduler.scheduler.add_job')
    def test_schedule_task(self, mock_add_job):
        # Define the task and time
        task = "Meeting with client"
        reminder_time = datetime(2024, 9, 20, 12, 0, 0)
        
        # Call the scheduling function
        schedule_task(task, reminder_time)
        
        # Assert that add_job was called once with the correct arguments
        mock_add_job.assert_called_once()

        args, kwargs = mock_add_job.call_args
        self.assertEqual(args[0].__name__, 'reminder')  # The function name that was passed
        self.assertEqual(kwargs['run_date'], reminder_time)

if __name__ == '__main__':
    unittest.main()
