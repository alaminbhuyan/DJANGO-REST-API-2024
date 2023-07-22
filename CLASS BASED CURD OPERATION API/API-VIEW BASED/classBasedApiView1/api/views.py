from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Item
from api.serializers import ItemSerializer

# Create your views here.
class ApiOverView(APIView):
    # To show all the api end points
    def get(self, request):
        api_urls = {
        'all_items': 'api/',
        'Search by Category': 'api/?category=category_name',
        'Search by Subcategory': 'api/?subcategory=category_name',
        'Add': 'api/create',
        'Update': 'api/update/pk',
        'Delete': 'api/item/delete/pk'}
        
        return Response(data=api_urls)

# This view_items function will either show all the data or filtered data queried by the user according to the category, subcategory, or name.
class ShowAllItemsApiView(APIView):
    def get(self, request, format=None):
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

# To create new Item
class AddItemApiView(APIView):
    def post(self, request, format=None):
        item = ItemSerializer(data=request.data)
        
        # validating for already existing data
        if Item.objects.filter(**request.data).exists():
            raise serializers.ValidationError(detail="This Item already Exists")
        
        if item.is_valid():
            item.save()
            return Response(data={"message" : "Item created Successfully", "data" : item.data})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# To delete Item
class UpdateItemApiView(APIView):
    def put(self, request, pk=None, format=None):
        # existing data
        item = Item.objects.get(pk=pk)
        # request.data contain the new updated data
        data = ItemSerializer(instance=item, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data={"message" : "Item Updated Successfully", "data" : data.data})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# To delete Item
class DeleteItemApiView(APIView):
    def delete(self, request, pk=None, format=None):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(data={"message" : "Item deleted successfully"}, status=status.HTTP_202_ACCEPTED)