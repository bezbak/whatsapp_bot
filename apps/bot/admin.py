from django.contrib import admin
from apps.bot.models import Menu, Order, MenuToOrder
# Register your models here.
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(MenuToOrder)