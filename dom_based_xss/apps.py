from django.apps import AppConfig


class DomBasedXssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dom_based_xss'
