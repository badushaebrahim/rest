from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def item_all(request):
    return Response("hello")