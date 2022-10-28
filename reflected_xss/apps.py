from django.apps import AppConfig


class ReflectedXssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reflected_xss'
