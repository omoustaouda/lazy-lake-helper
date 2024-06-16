import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.handlers import start, handle_message
from src.scheduler import setup_scheduler
from config.config import Config

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='logs/bot.log'
)

def main():
    updater = Updater(Config.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Set up reminders
    setup_scheduler()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
