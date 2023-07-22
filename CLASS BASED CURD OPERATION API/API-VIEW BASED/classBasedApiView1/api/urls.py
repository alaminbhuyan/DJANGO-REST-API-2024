from django.urls import path
from api import views


urlpatterns = [
    path(route="", view=views.ApiOverView.as_view(), name="home"),
    path(route="showItems/", view=views.ShowAllItemsApiView.as_view(), name="showItems"),
    path(route="create/", view=views.AddItemApiView.as_view(), name="addNewItem"),
    path(route="update/<int:pk>/", view=views.UpdateItemApiView.as_view(), name="updateItem"),
    path(route="delete/<int:pk>/", view=views.DeleteItemApiView.as_view(), name="deleteItem"),
]
