from rest_framework.decorators import api_view
from apps.bot.models import Order, Menu,MenuToOrder
from twilio.rest import Client
from core.config import account_sid1, auth_token1
from django.http import HttpResponse
from .answers import hello_text2,command2
client = Client(account_sid1, auth_token1)
# Create your views here.
item =0
step = 0
dish1 =MenuToOrder.objects.last() 
@api_view(['POST', "GET"])
def incoming(request):
    global step
    text = request.POST.get('Body').lower()
    phone_number = request.POST.get('From')
    if step == 0:
        hello_text(phone_number)
    elif step ==1:
        get_menu(phone_number, text)
    elif step == 2:
        create_order(phone_number,text)
    elif step ==3:
        set_order(phone_number, text)
    return HttpResponse({'200':'OK'})
    
def hello_text(phone_number):
    global step
    send_message(phone_number, hello_text2)
    step +=1
def create_order(phone_number, order): 
    global step
    global dish1
    global item
    try:
        item = Menu.objects.get(id = int(order))
        order2 = Order.objects.create(phone_number=phone_number, sum_of_order = 0)
        dish1=order2
        step +=1
        send_message(phone_number,'Выберите количество порций')
    except Exception as ex:
        print(ex)
        send_message(phone_number,'Такого номера нет. Напишите другой номер')

def set_order(phone_number, text):
    global step
    global item
    global dish1
    order = dish1
    if 'нет' in text:
        try:
            order.one_order.last.delete()
            step -=1
            send_message(phone_number,'Хорошо выберите другое блюдо')
        except:
            send_message(phone_number,'Хорошо выберите другое блюдо')
    elif 'отмена' in text:
        order.delete()
        step =0
        send_message(phone_number,'Ваш заказ отменён')
    elif 'ок' in text:
        step = 0
        message = f"""Пришёл заказ: {', '.join(' '.join((i.dish.name,'Количество:',i.count)) for i in order.one_order.all())}\nСумма заказа:{order.sum_of_order}\nНомер телефона:{phone_number}"""
        send_message('whatsapp:+99778010039', message=message)
    else:
        print([(i.dish.name,i.count) for i in order.one_order.all()], 'test')
        dish = MenuToOrder.objects.create(dish=item, order=order,count = int(text))
        dish.save()
        message = f"""✅✅✅ВАШ ЗАКАЗ✅✅✅\n\n{', '.join(' '.join((i.dish.name,'Количество:',i.count)) for i in order.one_order.all())}\n\nСумма:{order.sum_of_order}\n\n     🔥🔥🔥ДОБАВИТЬ ЕЩЁ, НАПИШИТЕ НОМЕР БЛЮДА🔥🔥🔥  \n\n🤝🤝🤝ОФОРМИТЬ ЗАКАЗ🤝🤝🤝 отправьте «ОК»\n\nНапишите 'нет' чтобы отменить выбор или 'Отмена' чтобы отменить заказ"""
        send_message(phone_number,message)

            
def get_menu(phone_number, text):
    global step
    if text == "1":
        for i in Menu.objects.all():
            message = f"""{i.id}\n{i.name}\n{i.description}\n{i.price}"""
            media = f"http://80.90.184.58:8000{i.image.url}"
            send_message(phone_number,message, media)
            step =2
    else:
        send_message(phone_number,command2)
        step =5
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
