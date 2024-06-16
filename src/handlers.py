from telegram import Update
from telegram.ext import CallbackContext
from modules.chores.chores import get_chores_message
from modules.reminders.reminders import get_pickup_reminder

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am the Lazy Lake Helper bot.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = "This is a placeholder response."

    if "chores" in user_message.lower():
        response = get_chores_message()
    elif "pickup" in user_message.lower():
        response = get_pickup_reminder()

    update.message.reply_text(response)
