from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View
from django.core.exceptions import ValidationError
from django.contrib.auth import login,logout,authenticate

#local imports 

from .serializer import User_serializer
from core.utils import Manage_base_view,confirm_tokens
# 3rd party imports

from rest_framework.views import APIView,Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token


User = get_user_model()

class User_actions(Manage_base_view):

    def user_registration(self,request,*args,**kwargs):
        data = {}
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            user_instance = serializer.save()
            token = Token.objects.get_or_create(user=user_instance)[0].key
            print(Token.objects.get_or_create(user=user_instance),'11111')
            data['status'] = 1
            data['message_en'] = 'User registration successfull'
            data['email'] = user_instance.email
            data['username'] = user_instance.username
            data['token'] = token
        else:
            data = serializer.errors
            print('this')
        return Response(data)



    def user_login(self,request,*args,**kwargs):
        data = {}
        email = request.data.get('email')
        password = request.data.get('password')
        is_auth = authenticate(email=email,password= password)
        if is_auth is not None:
            token = Token.objects.get_or_create(user=is_auth)[0].key
            login(request,is_auth)
            data['status'] =1
            data['message_en'] = 'Login Success'
            data['detail'] = {'email':is_auth.email,"token":token}
            return Response(data)
        else:
            data['status'] = 0
            data['message_en'] = "Login Failed"
            data['detail'] = "Invalid credentials"
            return Response(data)
        

    
    def delete_user(self,request,*args,**kwargs):
        data = {}
        permission_classes=[IsAuthenticated]
        email = request.data.get('email')
        try:
            account = User.objects.get(email=email)
        except:
            data['status'] = 0
            data['message_en'] = 'User does not exist'
            data['detail'] = " "
            return Response(data)
        
        
        if account.is_active:
            if confirm_tokens(request.auth,account.get_token()):
                account.delete()
                # token = 
                data['status'] = 1
                data['message_en'] = 'User delete Success'
                data['detail']='User delete successfull'
                return Response(data)
            else:
                data['status'] = 0
                data['message_en'] = 'Unauthorised'
                data['detail']='You are unauthorised to perform this action'
                return Response(data)
        else:
            data['status'] = 0
            data['message_en'] = 'User delete Unsuccessfull'
            data['detail']='User is not active'
            return Response(data)


    def get_user(self,request,*args,**kwargs):
        data = {}
        permission_classes = [IsAuthenticated]
        slug_field = request.data.get('slug_field')
        try:
            account = User.objects.get(slug_field=slug_field)
        except:
            data['status'] = 0
            data['message_en'] = 'User does not exist'
            data['detail'] = " "
            return Response(data)
        
        
        if account.is_active:
            if confirm_tokens(request.auth,account.get_token()):
                serializer = User_serializer(account)
                # token = 
                data['status'] = 1
                data['message_en'] = 'Success'
                data['detail']=serializer.data
                return Response(data)
            else:
                data['status'] = 0
                data['message_en'] = 'Unauthorised'
                data['detail']='You are unauthorised to perform this action'
                return Response(data)
        else:
            data['status'] = 0
            data['message_en'] = 'Failed'
            data['detail']='User is not active'
            return Response(data)
        

    def update_user(self,request,*args,**kwargs):
        data = {}
        permission_classes = [IsAuthenticated]
        slug_field = request.data.get('slug_field',None)
        if slug_field:
            try:
                account = User.objects.get(slug_field=slug_field)
            except:
                data['status'] = 0
                data['message_en'] = 'User does not exist'
                data['detail'] = " "
                return Response(data)
            
            
            if account.is_active:
                if confirm_tokens(request.auth,account.get_token()):
                    serializer = User_serializer(instance=account,data = request.data,partial=True)
                    if serializer.is_valid():
                        # token = 
                        serializer.save()
                        data['status'] = 1
                        data['message_en'] = 'Success'
                        data['detail']=serializer.data
                    else:
                        data['status'] = 0
                        data['message_en'] = 'Fail'
                        data['detail']=serializer.errors
                    return Response(data)
                else:
                    data['status'] = 0
                    data['message_en'] = 'Unauthorised'
                    data['detail']='You are unauthorised to perform this action'
                    return Response(data)
            else:
                data['status'] = 0
                data['message_en'] = 'Failed'
                data['detail']='User is not active'
                return Response(data)

        else:
            data['status'] = 0
            data['message_en'] = "Please check the user details provided"
            data['detail'] = " "
            return Response(data)




 
