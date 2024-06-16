from modules.chores.models import Chore, session

def get_chores_message():
    chores = session.query(Chore).all()
    return "Weekly Chores:\n" + "\n".join([f"{chore.name}: {chore.task}" for chore in chores])

def send_chores_reminder():
    # Logic to send chores reminder
    pass

# Add more functions as needed
