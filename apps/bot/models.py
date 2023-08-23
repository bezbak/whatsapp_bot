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

    def __str__(self):
        return f"{self.name} -- {self.price}"
    
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
    def __str__(self):
        return f"{self.dish.name}--{self.count}: {self.phone_number}"
    
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

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if self.order.sum_of_order==0:
            self.order.sum_of_order += self.dish.price * self.count
        return super().save(force_insert, force_update, using, update_fields)
    