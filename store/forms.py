from django.forms import ModelForm, Form, IntegerField
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["picture", "name", "brand", "price"]

class CartItemQuantityForm(Form):
    quantity = IntegerField(label="quantity")