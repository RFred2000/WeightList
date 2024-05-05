from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
