from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import itemSerializer
from rest_framework import serializers
from rest_framework import status
from .models import item
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def Apiview(request):
    api_urls = {
      'all_items': '/all',
      'Search by itemdis': '/?itemdis=itemdis_name',
      'Search by itemname': '/?itemname=itemname_name',
      'Add': '/create',
      'Update': '/update/pk',
      'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)
@api_view(['POST'])
def additems(request):
    items = itemSerializer(data=request.data)
 
    # validating for already existing data
    if item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if items.is_valid():
        items.save()
        return Response(items.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET'])
def viewitems(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = item.objects.filter(**request.query_params.dict())
    else:
        items = item.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = itemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    
@api_view(['POST'])
def updateitems(request, pk):
    Item = item.objects.get(pk=pk)
    data = itemSerializer(instance=Item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    
@api_view(['DELETE'])
def deleteitems(request, pk):
    Item = get_object_or_404(item, pk=pk)
    Item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)