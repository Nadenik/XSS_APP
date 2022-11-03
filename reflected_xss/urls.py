from django.urls import path
from .views import *


urlpatterns = [
    path('reflected_xss', reflected_xss_view, name='reflected_xss'),
    path('reflected_xss/introduction', introduction_view, name='reflected_xss_introduction'),
    path('reflected_xss/level1', level1_view, name='reflected_xss_level1'),
    path('reflected_xss/level2', level2_view, name='reflected_xss_level2')
]