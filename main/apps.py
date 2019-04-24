from django.apps import AppConfig
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


    
class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals  # noqa