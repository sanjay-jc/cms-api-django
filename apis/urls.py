from django.urls import path

from .views import *

urlpatterns = [
    path('create_blog',Blog_actions.as_view(method_name="create_blog"),name="create_blog"),
    path('get_blog',Blog_actions.as_view(method_name="get_blog"),name="get_blog"),
    path('update_blog',Blog_actions.as_view(method_name="update_blog"),name="update_blog"),
    path('delete_blog',Blog_actions.as_view(method_name="delete_blog"),name="delete_blog"),
    path('get_all_blogs',Blog_actions.as_view(method_name="get_all_blogs"),name="get_all_blogs"),
]