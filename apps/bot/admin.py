from django.contrib import admin
from apps.bot.models import Menu, Order, MenuToOrder, Category
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_filter = ["draft"]
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order)
admin.site.register(MenuToOrder)
admin.site.register(Category)