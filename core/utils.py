from django.db import models


STATUS_CHOICES = (
    (True,"Active"),
    (False,"Inactive")
)

class Active_objects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)


class Base_model(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,choices=STATUS_CHOICES)

    is_active = Active_objects() #custom manager to  filter the active objects
    objects = models.Manager()#default manager


    class Meta:
        abstract = True

