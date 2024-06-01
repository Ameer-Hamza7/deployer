from django.apps import AppConfig
from django.db.models.signals import post_save


class DeployEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deploy_engine'

    def ready(self):
        from .signals import handle_model_save
        post_save.connect(handle_model_save)
