from django.urls import path
from .views import *


urlpatterns = [
    path('stored_xss', stored_xss_view, name='stored_xss'),
    path('stored_xss/introduction', introduction_view, name='stored_xss_introduction'),
    path('stored_xss/level1', level1_view, name='stored_xss_level1'),
    path('stored_xss/level2', level2_view, name='stored_xss_level2'),
    # create comment endpoints
    path('stored_xss/level1_create_comment', level1_create_comment, name='stored_xss_level1_create_comment'),
    path('stored_xss/level2_create_comment', level2_create_comment, name='stored_xss_level2_create_comment'),
    # delete comment endpoints
    path('stored_xss/level1_delete_comment/<int:id>', level1_delete_comment, name="stored_xss_level1_delete_comment"),
    path('stored_xss/level2_delete_comment/<int:id>', level2_delete_comment, name="stored_xss_level2_delete_comment")
]