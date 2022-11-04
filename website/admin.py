from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ReflectedXssModule)
admin.site.register(DomBasedXssModule)
admin.site.register(StoredXssModule)
