from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(verbose_name="employee Name", max_length=60)
    age = models.CharField(verbose_name="employee Age", max_length=10)
    address = models.TextField(verbose_name="employee address")