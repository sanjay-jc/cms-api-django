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
    is_private = models.BooleanField(default=False)


    def save(self,*args,**kwargs):
        if not self.slug_field:
            self.slug_field = slugify((self.title)[:20]+str(uuid.uuid4())[:10])

        return super().save(*args,**kwargs)
    
    def get_like_count(self):
        result = Like.is_active.filter(blog_id=self).count()
        return result
    
    def __str__(self):
        return self.title
    

class Like(Base_model):
    blog_id = models.ForeignKey(Blog_model,on_delete=models.CASCADE)
    user_id = models.ForeignKey(user,on_delete=models.SET_NULL,null=True)
