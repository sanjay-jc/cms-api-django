from django.contrib import admin
from django.contrib.auth import get_user_model

user = get_user_model()
# Register your models here.

@admin.register(user)
class User_admin(admin.ModelAdmin):
    model = user
    list_display = ["email","username",'is_active']
    list_display_links = ("email","username")


