from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MelkaJewellery.accounts'

    def ready(self):
        import MelkaJewellery.accounts.signals
