from rest_framework.decorators import api_view
from apps.bot.models import Order, Menu,MenuToOrder, Category
from twilio.rest import Client
from core.config import account_sid1, auth_token1
from django.http import HttpResponse
from .answers import hello_text2,command2
client = Client(account_sid1, auth_token1)
# Create your views here.
item =0
step = 0
dish1 =0
is_order = False
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
    elif step ==4:
        del_order(phone_number, text)
    elif step ==5:
        if 'ок' in text:
            message = f"""Пришёл заказ на козу гриль!!!\n\nНомер телефона:{phone_number}"""
            send_message('whatsapp:+996557500113', message=message)
            send_message(phone_number, message='Мы приняли ваш заказ, ожидайте')
        else:
            step=0
            hello_text(phone_number)
    else:
        step=0
        hello_text(phone_number)

    return HttpResponse({'200':'OK'})
    
def hello_text(phone_number):
    global step
    send_message(phone_number, hello_text2)
    step +=1
def create_order(phone_number, order): 
    global step
    global dish1
    global item
    global is_order
    if is_order:
        try:
            item = Menu.objects.get(new_id = int(order))
            step +=1
            send_message(phone_number,'Выберите количество порций')
        except:
            send_message(phone_number,'Такого номера нет. Напишите другой номер')
    else:
        try:
            item = Menu.objects.get(new_id = int(order))
            order2 = Order.objects.create(phone_number=phone_number, sum_of_order = 0)
            dish1=order2
            step +=1
            send_message(phone_number,'Выберите количество порций')
        except:
            send_message(phone_number,'Такого номера нет. Напишите другой номер')

def set_order(phone_number, text):
    global step
    global item
    global is_order
    global dish1
    order = dish1
    dish = MenuToOrder.objects.create(dish=item, order=order,count = int(text))
    dish.save()
    order.sum_of_order += dish.dish.price * int(text)
    message = f"""✅✅✅ВАШ ЗАКАЗ✅✅✅\n\n{', '.join(' '.join((i.dish.name,'Количество:',str(i.count))) for i in order.one_order.all())}\n\nСумма:{order.sum_of_order} сом\n\n     🔥🔥🔥ДОБАВИТЬ ЕЩЁ, НАПИШИТЕ НОМЕР БЛЮДА🔥🔥🔥  \n\n🤝🤝🤝ОФОРМИТЬ ЗАКАЗ🤝🤝🤝 отправьте «ОК»\n\nНапишите 'нет' чтобы отменить выбор\n\n'Отмена' чтобы отменить заказ"""
    is_order = True
    send_message(phone_number,message)
    step=4

def del_order(phone_number, text):
    global step
    global item
    global is_order
    global dish1
    order = dish1
    if 'нет' in text.lower():
        try:
            order.sum_of_order -= order.one_order.latest('id').dish.price * order.one_order.latest('id').count
            order.one_order.latest('id').delete()
            print('order is delete')
            send_message(phone_number,'Хорошо выберите другое блюдо')
            step -=2
        except:
            send_message(phone_number,'Хорошо выберите другое блюдо')
    elif 'отмена' in text.lower():
        is_order = False
        order.delete()
        send_message(phone_number,'Ваш заказ отменён')
        step =0
    elif 'ок' in text.lower():
        is_order = False
        message = f"""Пришёл заказ: {', '.join(' '.join((i.dish.name,'Количество:',str(i.count))) for i in order.one_order.all())}\nСумма заказа:{order.sum_of_order} сом\nНомер телефона:{phone_number}"""
        send_message('whatsapp:+996557500113', message=message)
        send_message(phone_number, message='Мы приняли ваш заказ, ожидайте ответа')
        step = 0
    else:
        step =2
        create_order(phone_number, text)
def get_menu(phone_number, text):
    global step
    if text == "1":
        all_menu = ''
        for cat in Category.objects.all():
            cat_text = f"⭐️⭐️ {cat.name} ⭐️⭐️\n\n"
            for i,val in enumerate(cat.products.all().filter(draft = False)):
                if val == cat.products.all().latest('id'):
                    message = f"""\n{val.new_id}. {val.name} - {val.price}сом\n\n"""
                else:
                    message = f"""\n{val.new_id}. {val.name} - {val.price}сом"""
                cat_text += message
            all_menu+=cat_text
        send_message(phone_number, all_menu)
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
