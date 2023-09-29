from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name='Название блюдо',max_length=1555)
    price = models.DecimalField(verbose_name='Цена',max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='menu_images/')
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
        
class Cart(models.Model):
    menu_item = models.ForeignKey(
        Product, 
        verbose_name="Меню",
        related_name='menu_item',
        on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    username = models.CharField(verbose_name='Имя',max_length=1555, unique=True)
    phone = models.CharField(verbose_name='Телефонный номер',max_length=50)
    address = models.CharField(verbose_name='Адрес',max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def calculate_total_amount(self):
        return self.menu_item.price * self.quantity
    
    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_amount()
        super(Cart, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Данные клиента"
        verbose_name_plural = "Данные клиента"
        
# class CartItem(models.Model):
#     cart = models.ForeignKey(
#         Cart, 
#         verbose_name="Корзина",
#         related_name='cart',
#         on_delete=models.CASCADE)
    

#     class Meta:
#         verbose_name = "Корзина"
#         verbose_name_plural = "Корзина"
