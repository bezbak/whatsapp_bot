from rest_framework import serializers
from django.core.mail import send_mail
from .models import Product,Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
        
class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ('menu_item', 'quantity', 'username', 'phone','address','created_at','total_price')
        
    def get_total_price(self, obj):
        return obj.menu_item.price * obj.quantity
        
def send_order_email(order):
    subject = 'Новый заказ'
    message = f"""
    Новый заказ:
        Название : {order.menu_item.name}
        Цена: {order.menu_item.price}
        Количество: {order.quantity}
        Общая сумма: {order.total_price}
        Данные клиента:
        Имя: {order.username}
        Телефонный номер: {order.phone}
        Адрес: {order.address}
        """
    from_email = 'your_email@example.com'
    recipient_list = ['jamankulova.ayana283@gmail.com']  # Замените на адрес администратора
    
    send_mail(subject, message, from_email, recipient_list)


    

