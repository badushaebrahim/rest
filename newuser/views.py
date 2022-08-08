from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Items
from .serializer import Item_serializers
# Create your views here.


@api_view(['GET','POST'])
def item_all(request):
    if request.method == 'GET':
        data =Items.objects.all()
        serialize_data = Item_serializers(data,many=True)
        return Response(serialize_data.data)
    
    elif request.method == 'POST':
        serial = Item_serializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
