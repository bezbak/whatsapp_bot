# Generated by Django 4.2.4 on 2023-08-23 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_rename_text_order_count_order_dish_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='count',
        ),
        migrations.RemoveField(
            model_name='order',
            name='dish',
        ),
        migrations.AddField(
            model_name='order',
            name='sum_of_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='MenuToOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_dish', to='bot.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='one_order', to='bot.order')),
            ],
        ),
    ]
