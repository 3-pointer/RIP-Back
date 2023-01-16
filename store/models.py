from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(default=None)

    class Meta:
        managed = True    
        db_table = 'items'

class Order(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.TextField()
    order_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'orders'


