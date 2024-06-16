from modules.reminders.models import Reminder, session

def get_pickup_reminder():
    reminders = session.query(Reminder).all()
    return "Pickup Reminders:\n" + "\n".join([f"{reminder.item}: {reminder.location}" for reminder in reminders])

def send_pickup_reminder():
    # Logic to send pickup reminder
    pass

# Add more functions as needed
