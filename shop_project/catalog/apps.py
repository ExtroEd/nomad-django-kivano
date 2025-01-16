from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.db.backends.signals import connection_created
from django.db.models.signals import post_migrate
from django.core.management import call_command


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    verbose_name = _("Catalog")

    def ready(self):
        # Вместо вызова функции load_categories, используем команду
        post_migrate.connect(self.load_categories, sender=self)

    def load_categories(self, **kwargs):
        # Вызов команды из management/commands/load_categories
        call_command('load_categories')


def set_encoding(sender, connection, **kwargs):
    connection.connection.set_client_encoding('UTF8')


connection_created.connect(set_encoding)
