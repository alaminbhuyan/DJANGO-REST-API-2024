from django.contrib import admin
from api.models import Item


# Register your models here.
@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'subcategory', 'amount']