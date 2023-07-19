from django.contrib import admin
from api.models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'age', 'address']