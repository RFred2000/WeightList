from django.urls import path

from . import views

app_name = "store"
urlpatterns = [
    # Item CRUD API
    path("store_front", views.storeFront, name="store_front"),
    path("item_detail/<int:item_id>", views.itemDetail, name="item_detail"),
    path("create_item", views.createItem, name="create_item"),
    path("delete_item/<int:item_id>", views.deleteItem, name="delete_item"),
    path("update_item/<int:item_id>", views.updateItem, name="update_item"),
    
    # CartItem CRUD API
    path("view_cart", views.view_cart, name="view_cart"),
    path("add_to_cart/<int:item_id>", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:cart_item_id>", views.remove_from_cart, name="remove_from_cart")
]