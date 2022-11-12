from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('learn/', learn_view, name='learn'),
    path('profile/', profile_view, name='profile'),
    path('rules/', rules_view, name='rules')
]