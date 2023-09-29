# Generated by Django 4.2.5 on 2023-09-22 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1555, verbose_name='Название блюдо')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.FileField(upload_to='menu_images/')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=1555, unique=True, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефонный номер')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='menu.product', verbose_name='Меню')),
            ],
            options={
                'verbose_name': 'Данные клиента',
                'verbose_name_plural': 'Данные клиента',
            },
        ),
    ]