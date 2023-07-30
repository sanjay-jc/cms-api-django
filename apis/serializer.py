#local imports

from .models import Blog_model,Like


#3rd party imports

from rest_framework import serializers 
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


class Blog_serializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Blog_model
        fields = ["title","description","content","image","like_count","slug_field"]


    def get_like_count(self,obj):
        return obj.get_like_count()
    
