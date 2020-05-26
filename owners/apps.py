from django.apps import AppConfig


class OwnersConfig(AppConfig):
    name = 'owners'

    def ready(self):
        from . import signals
        