from django.apps import AppConfig


class SkyusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skyusers'

    def ready(self):
        import skyusers.signals
