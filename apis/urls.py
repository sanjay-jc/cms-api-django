from django.urls import path

from .views import *

urlpatterns = [
    #blog actions urls

    path('create_blog',Blog_actions.as_view(method_name="create_blog"),name="create_blog"),
    path('get_blog',Blog_actions.as_view(method_name="get_blog"),name="get_blog"),
    path('update_blog',Blog_actions.as_view(method_name="update_blog"),name="update_blog"),
    path('delete_blog',Blog_actions.as_view(method_name="delete_blog"),name="delete_blog"),
    path('get_all_blogs',Blog_actions.as_view(method_name="get_all_blogs"),name="get_all_blogs"),


    #like action urls
    path('create_like',Like_actions.as_view(method_name="create_like"),name="create_like"),
    path('delete_like',Like_actions.as_view(method_name="delete_like"),name="delete_like"),
]