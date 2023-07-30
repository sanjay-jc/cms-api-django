from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Custom_user_manager
from uuid import uuid4

#3rd party imports 

from rest_framework.authtoken.models import Token

class Custom_user(AbstractUser):

    email = models.EmailField(unique=True)
    slug_field = models.SlugField(max_length=50,null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.slug_field:
            self.slug_field = str(uuid4())[:10]
        return super().save(*args,**kwargs)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]

    objects = Custom_user_manager()


    def __str__(self):
        return self.email

    def get_token(self):
        try:
            token = Token.objects.get_or_create(user=self)[0].key
            return token
        except Exception as e:
            return False