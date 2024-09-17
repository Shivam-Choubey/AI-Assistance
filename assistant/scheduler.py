from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

scheduler = BackgroundScheduler()

def schedule_task(task, reminder_time):
    def reminder():
        print(f"Reminder: {task}")
    scheduler.add_job(reminder, 'date', run_date=reminder_time)
    scheduler.start()
