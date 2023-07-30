from django.contrib import admin

# Register your models here.

from .models import Blog_model,Like

@admin.register(Blog_model)
class Blog_admin(admin.ModelAdmin):
    model = Blog_model
    list_display = ["title","status","created_by","is_private"]


@admin.register(Like)
class Like_admin(admin.ModelAdmin):
    model = Like
    list_display = ("blog_id","user_id",'status')

