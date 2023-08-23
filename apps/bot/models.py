from typing import Iterable, Optional
from django.db import models

# Create your models here.
class Menu(models.Model):
    image = models.ImageField(
        upload_to='menu/'
    )
    name = models.CharField(
        max_length=50
    )
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Меню"

class Order(models.Model):
    sum_of_order = models.PositiveIntegerField(
        default=0
    )
    phone_number = models.CharField(
        max_length=15
    )
    
    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"

class MenuToOrder(models.Model):
    dish = models.ForeignKey(
        Menu,
        related_name='order_dish',
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order,
        related_name='one_order',
        on_delete= models.CASCADE
    )
    count = models.PositiveIntegerField(
        default=1
    )
