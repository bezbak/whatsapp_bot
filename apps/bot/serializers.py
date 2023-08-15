from rest_framework import serializers
from apps.bot.models import Order

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"