hello_text = """
✅✅✅ Бул жерден сиз үйүңүзгө же жумушунузга жеткирүү буйуртсаныз болот 🚀🚀🚀

✅✅✅ Здесь вы можете заказать доставку на дом 🏠 🏠🏠 или на работу 👨‍🚒👨‍🚒👨‍🚒


1. Тамак тизмеси 📔📔📔
2. Козу гриль 🐏🐏🐏

1. Меню 📔📔📔
2. Ягнёнок на гриле 🐏🐏🐏

Буйуртма үчүн 1 же 2ни басыңыз 📌📌📌

Для заказа нажмите цифру 1 или  2 📌📌📌
"""
command2 = """
Цена козу гриль 
от 12000 до 20000 ( от 13кг до 24 кг) 🤩

УКРАШЕНИЕ + ДОСТАВКА по городу в ПОДАРОК 🎁


А кафе Тандыр эт на АРАВАНСКОМ   работает 🚀🚀🚀 для вашего удобства каждый день с 9:00 утра до 22:00 вечера 🔥🔥🔥
У нас имеется 

✅ ЖУПКА (Чабаты)
✅ КАТТАМА (с зел.луком или сахарной пудрой) 
✅БООРСОК 
✅ОПКО
✅ЧУЧУК
✅КАЙМАК 
✅ КЫМЫЗ

И мн. Другое рады вашим заказам ❤️❤️❤️

Для заказа звоните нам:
 +996 558 775 858 
 или перейдите по ссылке на WhatsApp : 
📌 https://shorturl.at/msEQY

Если вы определились напишите *ок*
"""
menu = """
        ⭐️⭐️ЗАКУСКИ⭐️⭐️

1. Чучук 100гр  -  130 с 
2. Өпкө 100гр  - 80 с 
3. Жупка (Чабаты) 1шт - 35 с
4. Каттама  1шт - 80 с 
5. Боорсок 500 гр - 150 с 
6. Нан 1 шт - 40 с
7. Каймак 100гр - 80 с
8. Чөбөгө 80 гр - 80 с
9. Картофель фри 100гр - 90 с


        ⭐️⭐️САЛАТЫ ⭐️⭐️

10. Острый салат - 230с
11. Колхозный с майонезом- 200с
12. Овощной - 180с
13. Мужской каприз - 250с
14. Греческий - 220с

        ⭐️⭐️СУПЫ⭐️⭐️
15. Суп с фрикадельками - 130с
16. Суп лапша из курицы - 130с
17. Суп куриный - 150с
18. Борщ - 140с
19. Шорпо из баранины - 180с
20. Шорпо из говядины - 180с
21. Мясо по казахски - 160с 
22. Домашние Пельмени - 160с

        ⭐️⭐️ГОРЯЧИЕ БЛЮДА⭐️⭐️ 
23. Гуляш - 180с
24. Тефтели - 160с
25. Чахахбили из курицы - 180с
26. Тандыр тоок 300гр - 220с 
27. Тандыр эт - 300гр - 390с
28. Бифштекс - 180с
29. Оромо 3шт. - 120с
30. Манты  - 175с 1шт 35с


        ⭐️⭐️НАПИТКИ⭐️⭐️
31. Курут  - 1л - 150с 
32. Кымыз - 1л - 200с 
33. Легенда б/г - 1л - 50с
34. Липтон -  1л - 90
35. ASU в асс. 0,5 - 40
36.                   1л - 60 
37. Пепси 1л - 100с
38.                  2л - 180с

Буйуртма үчүн керектүү команданы тандап санын кошо жазыныз 🍔🍔🍔 

Для заказа нажмите на нужную команду и количество порции 🥑🥑🥑

    
✨✨БУЙУРТМА КАБЫЛ КЫЛАБЫЗ✨✨

Козу гриль 🐏
Тоок гриль 🍗
Тандыр эт 🥩
Буйрак гриль 🐏
Таш-кордо🥩


 +996 557 77 58 58 ватсап 📳
 +996 554 00 58 58

 +996 778 92 04 48 ватсап 
 +996 777 83 83 58

U_dadu_K
Kizu.grillosh инстаграмм
"""
set_order = """
Мы приняли ваш заказ, ожидайте
"""

dict_of_orders = {
        "1":'Чучук 100гр',
        "2":'Өпкө 100гр',
        "3":'Жупка (Чабаты)',
        "4":'Каттама',
        "5":'Боорсок 500г',
        "6":'Нан',
        "7":'Каймак 100гр',
        "8":'Чөбөгө 80гр',
        "9":'Картофель фри 100гр',
        "10":'Острый салат',
        "11":'Колхозный с майонезом',
        "12":'Овощной',
        "13":'Мужской каприз',
        "14":'Греческий',
        "15":'Суп с фрикадельками',
        "16":'Суп лапша из курицы',
        "17":'Суп куриный',
        "18":'Борщ',
        "19":'Шорпо из баранины',
        "20":'Шорпо из говядины',
        "21":'Мясо по казахски',
        "22":'Домашние Пельмени',
        "23":'Гуляш',
        "24":'Тефтели',
        "25":'Чахахбили из курицы',
        "26":'Тандыр тоок 300гр',
        "27":'Тандыр эт 300гр',
        "28":'Бифштекс',
        "29":'Оромо 3шт',
        "30":'Манты',
        "31":'Курут 1л',
        "32":'Кымыз 1л',
        "33":'Легенда б/г 1л',
        "34":'Липтон 1л',
        "35":'ASU в асс. 0,5л',
        "36":'ASU в асс. 1л',
        "37":'Пепси 1л',
        "38":'Пепси 2л'
}
dict_of_prices = {
        "1":130,
        "2":80,
        "3":35,
        "4":80,
        "5":150,
        "6":40,
        "7":80,
        "8":80,
        "9":90,
        "10":230,
        "11":200,
        "12":180,
        "13":250,
        "14":220,
        "15":130,
        "16":130,
        "17":150,
        "18":140,
        "19":180,
        "20":180,
        "21":160,
        "22":160,
        "23":180,
        "24":160,
        "25":180,
        "26":220,
        "27":390,
        "28":180,
        "29":120,
        "30":35,
        "31":150,
        "32":200,
        "33":50,
        "34":90,
        "35":40,
        "36":60,
        "37":100,
        "38":180
}