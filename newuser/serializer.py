from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Items

class Item_serializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id','title','discription','status']
        
