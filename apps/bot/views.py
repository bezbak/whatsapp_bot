from rest_framework.decorators import api_view
from apps.bot.models import Order
from twilio.rest import Client
from django.conf import settings
from core.config import account_sid1, auth_token1

client = Client(account_sid1, auth_token1)
# Create your views here.
@api_view(['POST', "GET"])
def test(request):
    print(request.POST.get('Body'))

@api_view(['POST', "GET"])
def test2(request):
    print(account_sid1)

    