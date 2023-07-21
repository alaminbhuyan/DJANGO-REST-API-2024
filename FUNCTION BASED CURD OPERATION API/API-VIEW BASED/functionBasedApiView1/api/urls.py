from django.urls import path
from api import views


urlpatterns = [
    path(route="", view=views.apiOverView, name="home"),
    path(route="allItems/", view=views.view_all_items, name="allItems"),
    path(route="create/", view=views.add_items, name="addItem"),
    path(route="update/<int:pk>/", view=views.update_items, name="updateItem"),
    path(route="delete/<int:pk>/", view=views.delete_items, name="deleteItem"),
]
