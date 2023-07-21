from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from api.models import Item
from api.serializers import ItemSerializer


# Show all the end points function view
@api_view(http_method_names=['GET'])
def apiOverView(request):
    api_urls = {
        'all_items': 'api/',
        'Search by Category': 'api/?category=category_name',
        'Search by Subcategory': 'api/?subcategory=category_name',
        'Add': 'api/create',
        'Update': 'api/update/pk',
        'Delete': 'api/item/delete/pk'
    }
    
    return Response(data=api_urls)

# Add New Item function view
@api_view(http_method_names=['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)
    
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError(detail="This data already Exists")
    
    if item.is_valid():
        item.save()
        return Response(data={"message" : "Item created Successfully", "data" : item.data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# This view_items function will either show all the data or filtered data queried by the user according to the category, subcategory, or name.
@api_view(http_method_names=['GET'])
def view_all_items(request):
    # Checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
    
    # If there is something in items else raise error
    if items:
        serializer = ItemSerializer(instance=items, many=True)
        return Response(data=serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(http_method_names=['PUT'])
def update_items(request, pk):
    # existing data
    item = Item.objects.get(pk=pk)
    # request.data contain the new updated data
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data={"message" : "Item Updated Successfully", "data" : data.data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Delete view
@api_view(http_method_names=['DELETE'])
def delete_items(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response(data={
        "message" : "Item deleted successfully"
    }, status=status.HTTP_202_ACCEPTED)