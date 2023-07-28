from django.contrib import admin

# Register your models here.

from .models import Blog_model

admin.site.register(Blog_model)