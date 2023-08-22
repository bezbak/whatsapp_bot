from rest_framework.decorators import api_view
from apps.bot.models import Order, Menu
from twilio.rest import Client
from core.config import account_sid1, auth_token1
from django.http import HttpResponse
client = Client(account_sid1, auth_token1)
# Create your views here.


@api_view(['POST', "GET"])
def hello_text(request):
    text = request.POST.get('Body')
    phone_number = request.POST.get('From')
    for i in Menu.objects.all():
        message = f"""{i.name}\n{i.description}\n{i.price}"""
        send_message(phone_number,message, {i.image.url})

    return HttpResponse({'200':'OK'})
@api_view(['POST', "GET"])
def test2(request):
    print(account_sid1)

def send_message(receiver_number, message, image):
    message = client.messages.create(
        body=message,
        from_='whatsapp:+996998767651',
        to=receiver_number,
        media_url=[image]
    )
    print(f"Сообщение отправлено. SID: {message.sid}")
