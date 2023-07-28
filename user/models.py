from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Custom_user_manager

class Custom_user(AbstractUser):

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]

    objects = Custom_user_manager()


    def __str__(self):
        return self.email
