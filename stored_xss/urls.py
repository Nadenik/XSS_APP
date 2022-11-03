from django.urls import path
from .views import *


urlpatterns = [
    path('stored_xss', stored_xss_view, name='stored_xss'),
    path('stored_xss/introduction', introduction_view, name='stored_xss_introduction'),
    path('stored_xss/level1', level1_view, name='stored_xss_level1'),
    path('stored_xss/level2', level2_view, name='stored_xss_level2')
]