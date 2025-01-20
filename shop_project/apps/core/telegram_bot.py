from telegram import Update
from telegram.ext import (Application, CommandHandler, MessageHandler, filters,
                          CallbackContext)
from decouple import config
import logging
from datetime import datetime

TOKEN = config('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

WORK_HOURS = {
    'monday_to_friday': (9, 19),
    'saturday': (9, 18),
    'sunday': (10, 17),
}


def is_work_time():
    now = datetime.now()
    day_of_week = now.weekday()
    hour = now.hour

    if day_of_week in range(0, 5):
        start, end = WORK_HOURS['monday_to_friday']
        if start <= hour < end:
            return True
    elif day_of_week == 5:
        start, end = WORK_HOURS['saturday']
        if start <= hour < end:
            return True
    elif day_of_week == 6:
        start, end = WORK_HOURS['sunday']
        if start <= hour < end:
            return True

    return False


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Здравствуйте! Я ваш помощник.")
    send_auto_reply(update)


async def send_auto_reply(update: Update):
    if is_work_time():
        await update.message.reply_text(
            "Здравствуйте! Мы скоро ответим вам в порядке очереди. Если у вас "
            "срочный вопрос, пожалуйста, позвоните нам по мобильной связи, "
            "попросив оператора с которым переписываетесь. Голосовые звонки в "
            "мессенджерах не поддерживаются, но вы можете отправить голосовое "
            "сообщение.\n\n"
            "0(312) 98-66-70\n"
            "0(555) 96-00-77\n"
            "0(770) 96-00-77\n"
            "0(700) 96-00-78")
    else:
        await update.message.reply_text(
            "Добрый день, сейчас нерабочее время, оставьте пожалуйста свое "
            "сообщение, мы получим его и обязательно ответим. График Пн-пт "
            "09-19; Сб 09-18; Вс 10-17.")


async def handle_message(update: Update, context: CallbackContext):
    await send_auto_reply(update)


async def error(update: Update, context: CallbackContext):
    logger.warning(f'Update {update} caused error {context.error}')


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                           handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
