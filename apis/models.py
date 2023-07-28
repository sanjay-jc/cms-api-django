from django.db import models
from core.utils import Base_model
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import uuid
user = get_user_model()

class Blog_model(Base_model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images')
    created_by = models.ForeignKey(user,on_delete=models.CASCADE)
    slug_field = models.SlugField(max_length=50,null=True,blank=True)


    def save(self,*args,**kwargs):
        if not self.slug_field:
            self.slug_field = slugify((self.title)[:20]+str(uuid.uuid4())[:10])

        return super().save(self,*args,**kwargs)