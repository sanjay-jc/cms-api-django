from django.contrib.auth.base_user import BaseUserManager

class Custom_user_manager(BaseUserManager):

    def create_user(self,email,password,*args,**kwargs):

        if not email:
            raise ValueError('Email field is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,email,password,*args,**kwargs):

        kwargs.setdefault("is_active",True)
        kwargs.setdefault("is_superuser",True)
        kwargs.setdefault("is_staff",True)

        if kwargs.get("is_staff") is not True:
            raise ValueError('is_staff must be set to true')
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError('is_superuser must be set to true')
        
        if kwargs.get("is_active") is not True:
            raise ValueError('is_active must be set to true')
        return self.create_user(email,password,*args,**kwargs)