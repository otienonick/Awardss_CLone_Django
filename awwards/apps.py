from django.apps import AppConfig


class AwwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awwards'

    def ready(self):
        import awwards.signals
