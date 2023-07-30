from django.db import models
from rest_framework.views import APIView,Response,Http404

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


class Manage_base_view(APIView):

    method_name = None
    template_name = None

    def get(self,request,*args,**kwargs):
        try:
            if self.method_name is not None:
                func  = getattr(self,self.method_name,None)
                print('func',func)
                if func is not None:
                    return func(request,*args,**kwargs)

        except:
            return Http404("Method GET not allowed")
        
    

    def post(self,request,*args,**kwargs):
        if self.method_name is not None:
            func = getattr(self,self.method_name,None)
            if func is not None:
                print(request)
                return func(request,*args,**kwargs)
        
        return Response({
            "status":0,
            "message_en":"Method not defined",
            "details":" "        
            })
    def put(self,request,*args,**kwargs):
        if self.method_name is not None:
            func = getattr(self,self.method_name,None)
            if func is not None:
                print(request)
                return func(request,*args,**kwargs)
        
        return Response({
            "status":0,
            "message_en":"Method not defined",
            "details":" "        
            })
    def patch(self,request,*args,**kwargs):
        if self.method_name is not None:
            func = getattr(self,self.method_name,None)
            if func is not None:
                print(request)
                return func(request,*args,**kwargs)
        
        return Response({
            "status":0,
            "message_en":"Method not defined",
            "details":" "        
            })
    


def confirm_tokens(token1,token2):
    return str(token1) == str(token2)