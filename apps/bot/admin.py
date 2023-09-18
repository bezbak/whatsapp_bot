from django.contrib import admin
from apps.bot.models import Menu, Order, MenuToOrder, Category
# Register your models here.

@admin.action(description="Добавить в черновик")
def make_unpublished(modeladmin, request, queryset):
    queryset.update(draft = True)

@admin.action(description="Убрать из черновика")
def make_published(modeladmin, request, queryset):
    queryset.update(draft = True)

class MenuAdmin(admin.ModelAdmin):
    list_filter = ["draft"]
    actions = [make_published, make_unpublished]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Order)
admin.site.register(MenuToOrder)
admin.site.register(Category)