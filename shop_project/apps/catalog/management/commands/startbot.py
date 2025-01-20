from django.core.management.base import BaseCommand
from apps.core.telegram_bot import main


class Command(BaseCommand):
    help = 'Запускает Telegram-бота'

    def handle(self, *args, **kwargs):
        self.stdout.write("Запуск Telegram-бота...")
        main()
