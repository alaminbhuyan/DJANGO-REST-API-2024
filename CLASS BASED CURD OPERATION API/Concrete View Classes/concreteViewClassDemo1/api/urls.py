from django.urls import path
from api import views


# app_name = 'api'

urlpatterns = [
    path(route="list/", view=views.EmployeeList.as_view(), name="listview"),
    path(route='create/', view=views.EmployeeCreate.as_view(), name='createview'),
    path(route='update/<int:id>', view=views.EmployeeUpdate.as_view(), name='updateview'),
    path(route='read/<int:id>', view=views.EmployeeRetrieve.as_view(), name='readview'),
    path(route='delete/<int:id>', view=views.EmployeeDelete.as_view(), name='deleteview'),
]
