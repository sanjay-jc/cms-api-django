from django.urls import path


#local imports
from .views import User_actions


urlpatterns = [
    path('registration',User_actions.as_view(method_name = 'user_registration'),name='registration'),
    path('login',User_actions.as_view(method_name = 'user_login'),name='login'),
    path('delete_user',User_actions.as_view(method_name = 'delete_user'),name='delete_user'),
    path('get_user',User_actions.as_view(method_name = 'get_user'),name='get_user'),
    path('update_user',User_actions.as_view(method_name = 'update_user'),name='update_user'),
]