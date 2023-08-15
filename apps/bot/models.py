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
    text = models.CharField(
        max_length=255
    )

    def __str__(self):
        return f"{self.text}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"