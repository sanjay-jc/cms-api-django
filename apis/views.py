
#local imports 

from core.utils import Manage_base_view
from .serializer import Blog_serializer
from .models import *
from core.utils import confirm_tokens

#3rd party imports

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response


class Blog_actions(Manage_base_view):

    def create_blog(self,request,*args,**kwargs):
        data = {}
        permission_classes = [IsAuthenticated]

        serializer = Blog_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)

            data['status']=1
            data["message_en"]="Blog creation successfull"
            data["detail"] = " "
            return Response(data)
        else:
            data['status']=1
            data["message_en"]="Fail"
            data["detail"] = serializer.errors
            return Response(data)
        
    def get_blog(self,request,*args,**kwargs):
        data = {}
        # permission_classes = [IsAuthenticated]

        blog_slug = request.data.get('slug_field')
        try:
            blog = Blog_model.is_active.get(slug_field = blog_slug)
        except:
            data['status'] = 0
            data['message_en'] = "Blog does not exist"
            data['detail'] = ''
            return Response(data)
        
        if blog.is_private: 
            token = confirm_tokens(request.auth,blog.created_by.get_token())
            if token:
                serializer = Blog_serializer(instance=blog,context = {"request":request})
                data['status'] = 1
                data['message_en'] = 'Success'
                data['detail'] = serializer.data
                return Response(data)
            else:
                data['status'] = 0
                data['message_en'] = 'Unauthorised'
                data['detail'] = "Cannot view a private blog"
                return Response(data)
        else:
            serializer = Blog_serializer(blog)
            data['status'] = 1
            data['message_en'] = 'Success'
            data['detail'] = serializer.data
            return Response(data)
        

    def update_blog(self,request,*args,**kwargs):
        data = {}
        permission_classes = [IsAuthenticated]

        blog_slug = request.data.get('slug_field')
        try:
            blog = Blog_model.is_active.get(slug_field = blog_slug)
        except:
            data['status'] = 0
            data['message_en'] = "Blog does not exist"
            data['detail'] = ''
            return Response(data)
        

        token = confirm_tokens(request.auth,blog.created_by.get_token())
        if token:
            serializer = Blog_serializer(instance=blog,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                data['status'] = 1
                data['message_en'] = 'Success'
                data['detail'] = serializer.data
                return Response(data)
            else:
                data['status'] = 0
                data['message_en'] = 'Fail'
                data['detail'] = serializer.errors
                return Response(data)
        else:
            data['status'] = 0
            data['message_en'] = 'Unauthorised'
            data['detail'] = "You are not authorised to perform this operation"
            return Response(data)
        

    def delete_blog(self,request,*args,**kwargs):
        data = {}
        permission_classes = [IsAuthenticated]

        blog_slug = request.data.get('slug_field')
        try:
            blog = Blog_model.is_active.get(slug_field = blog_slug)
        except:
            data['status'] = 0
            data['message_en'] = "Blog does not exist"
            data['detail'] = ''
            return Response(data)
        

        token = confirm_tokens(request.auth,blog.created_by.get_token())
        if token:

                blog.delete()
                data['status'] = 1
                data['message_en'] = 'Success'
                data['detail'] = " "
                return Response(data)
            
        else:
            data['status'] = 0
            data['message_en'] = 'Unauthorised'
            data['detail'] = "You are not authorised to perform this operation"
            return Response(data)
        

    def get_all_blogs(self,request,*args,**kwargs):
        data = {}
        try:
            blog = Blog_model.is_active.filter(is_private=False)
            serializer = Blog_serializer(instance=blog,many=True)
            data['status'] = 1
            data['message_en'] = 'Success'
            data['detail'] = serializer.data
            return Response(data)
        
        except Exception as e:
            print('sdfadd',str(e))
            data['status'] = 0
            data['message_en'] = "Blog does not exist"
            data['detail'] = ''
            return Response(data)
        
