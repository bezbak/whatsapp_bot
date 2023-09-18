from typing import Iterable, Optional
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Menu(models.Model):
    image = models.ImageField(
        upload_to='menu/',
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=50
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.SET_NULL,
        blank=True, 
        null=True,
        verbose_name='Категория'
    )
    price = models.IntegerField()
    draft = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}"
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
