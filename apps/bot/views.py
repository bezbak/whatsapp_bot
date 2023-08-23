from rest_framework.decorators import api_view
from apps.bot.models import Order, Menu
from twilio.rest import Client
from core.config import account_sid1, auth_token1
from django.http import HttpResponse
from .answers import hello_text2
client = Client(account_sid1, auth_token1)
# Create your views here.

step = 0
item = 0
last_sum = 0
order_sum = 0
order_dict = {}
@api_view(['POST', "GET"])
def incoming(request):
    global step
    text = request.POST.get('Body').lower()
    phone_number = request.POST.get('From')
    if step == 0:
        hello_text(phone_number)
    elif step ==1 and '1' in text:
        get_menu(phone_number)
    elif step == 2:
        get_order(phone_number,text)
    elif step ==3:
        set_order(phone_number, text)
    return HttpResponse({'200':'OK'})
    
def hello_text(phone_number):
    global step
    send_message(phone_number, hello_text2)
    step +=1
def get_order(phone_number, order):
    global step
    global item
    global last_sum
    try:
        item = Menu.objects.get(id = int(order))
        last_sum += item.price
        step +=1
        send_message(phone_number,'Выберите количество порций')
    except:
        send_message(phone_number,'Такого номера нет. Напишите другой номер')

def set_order(phone_number, text):
    global item
    global step
    global last_sum
    global order_sum
    if 'нет' in text:
        order_sum -= last_sum
        item = 0
        order_dict.popitem()
        step -=1
        send_message(phone_number,'Хорошо выберите другое блюдо')
    elif 'отменя' in text:
        item = 0
        last_sum = 0
        order_sum = 0
        order_dict = {}
        step =0
        send_message(phone_number,'Ваш заказ отменён')
    elif 'ок' in text:
        step = 0
        order = Order.objects.latest('id')
        text = f"""Пришёл заказ: {', '.join(' '.join((v,'Количество:',l)) for v,l in order.one_order.all())}\nСумма заказа:{order.sum_of_order}\nНомер телефона:{phone_number}"""
def get_menu(phone_number):
    for i in Menu.objects.all():
        message = f"""{i.id}\n{i.name}\n{i.description}\n{i.price}"""
        media = f"http://80.90.184.58:8000{i.image.url}"
        send_message(phone_number,message, media)

def send_message(receiver_number, message, image='no'):
    if image == 'no':
        message = client.messages.create(
            body=message,
            from_='whatsapp:+996998767651',
            to=receiver_number
        )
    else:
            message = client.messages.create(
            body=message,
            from_='whatsapp:+996998767651',
            to=receiver_number,
            media_url=[image]
        )
    print(f"Сообщение отправлено. SID: {message.sid}")
