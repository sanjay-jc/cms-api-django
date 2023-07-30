from django.contrib.auth import get_user_model
#3rd party imports 
from rest_framework import serializers

#local imports



User = get_user_model()


class User_serializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        extra_kwargs = {"password":{"write_only":True}}
        fields = ["username","email","password","slug_fiel"]

    def create(self,validated_data):
        password = validated_data.pop('password')

        user_instance = self.Meta.model(**validated_data)
        if password is not None:
            user_instance.set_password(password)
        user_instance.save()
        
        return user_instance
    



