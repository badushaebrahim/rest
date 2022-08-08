from pstats import Stats
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
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

class Item_by_one (APIView):
    
    def get(self,request,id):
        itemdata = valueget(id)
        itemserial = Item_serializers(itemdata)
        return Response(itemserial.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        itemdata = valueget(id)
        itemserial = Item_serializers(itemdata,data=request.data)
        if itemserial.is_valid():
            itemserial.save()
            return Response(itemserial.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        itemdata = valueget(id)
        itemdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    
    
    


def valueget(id):
        try:
            itemdata = Items.objects.get(pk=id)
            return itemdata
        except Items.DoesNotExist:
            return Response(stats=status.HTTP_404_NOT_FOUND)