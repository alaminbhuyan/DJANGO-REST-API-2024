from rest_framework import serializers
from api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ('category', 'subcategory', 'name', 'amount')
        fields = '__all__'