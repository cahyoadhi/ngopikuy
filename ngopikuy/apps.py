from django.apps import AppConfig

class NgopikuyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ngopikuy'

    def ready(self):
        import ngopikuy.controllers.signals