import schedule
import time
from modules.chores.chores import send_chores_reminder
from modules.reminders.reminders import send_pickup_reminder

def setup_scheduler():
    schedule.every().saturday.at("10:00").do(send_chores_reminder)
    schedule.every().wednesday.at("16:00").do(send_pickup_reminder)
    # Add more schedules as needed

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
