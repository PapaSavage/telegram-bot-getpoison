class Admin():
    curs = 12.9
    nacenka1 = 500
    nacenka2 = 1000
    nacenka3 = 2000
    nacenka4 = 2500
    nacenka5 = 3000
    prev_message = []

    message_hello = """
🤠 Нихао, {0}!
Добро пожаловать в нашу команду GET POIZON

Что сделать для тебя?
    """

    message_rasschet = ''' 
Введите цену на товар в <b>ЮАНЯХ</b>🇨🇳
и бот покажет цену с учётом доставки до склада в Москве
Внимание! Выбирайте цену, которая <b>ЗАЧЕРКНУТА</b> и находится <b>СЛЕВА</b>.
Система отображает скидки для первых покупателей. 

<b>У нас нет этих скидок!</b> 

                               '''
    message_order = '''
                    💎 Оформить заказ. 

Для заказа свяжитесь с менеджером, предоставьте фото товара и укажите ваш размер.

@Getpoizon_manager

                               '''

    message_scum = '''
                    Про скам🙈 

Друзья, прочтите всё внимательно до конца, это всё <b>очень важно</b>.
Все заказы делаются только через этот аккаунт:
@getpoizon_manager

Мы единственные во всей Российской Федерации, те кто <b>не скрывает своё истинное лицо</b>. И вы можете спокойно просмотреть наши личные социальные сети.

<b>Наши контакты:</b>
https://t.me/getpoizon_manager
https://t.me/alkkza
https://t.me/snimatos
<b>ОСТАЛЬНЫЕ ВСЕ - МОШЕННИКИ!</b>

                               '''
    message_course = '''
                    Про курс 💹

Почему у нас такой курс юаня?🇨🇳

Если вы задались таким вопросом, значит вы зашли на сайт Центробанка РФ и посмотрели официальный курс и увидели, что он отличается от нашего примерно на 2 рубля
(специально не приводим точных цифр, т.к. ситуация меняется каждый день)

Самый простой ответ на вопрос о высоком курсе:

❗️ В текущих реалиях нельзя купить валюту даже близко к курсу ЦБ.
Например, можно посмотреть по какой цене Сбербанк ПРОДАЕТ юань
Обычно это плюс 3,5 рубля к официальному курсу ЦБ

Но даже если предположить, что у вас есть юань в физическом(фиатном) виде - дальше его нужно отправить в Китай. Тут также в игру вступают посредники и курс сильно вырастет. 💴

Если у вас есть юань на брокерском счете (например, тинькоф) - попробуйте их вывести без потери хотябы 20%.📈

Мы стараемся закупать валюту максимально дешево и оперативно.

Какой будет курс завтра?💴🇨🇳💴

Мы не знаем также как и не знаете вы. Всем клиентам(хоть на 100 юаней, хоть на 100 000 юаней) мы советуем не ждать завтра, потому что завтра в большинстве случаев хуже. В таком мире живем.

                               '''

    message_commission = '''
    🌚 Наша комиссия, курс 

Комиссия❇️
Рассчитывается <i>каждому индивидуально</i>, потому что комиссия зависит от <i>цены товара</i> и от <i>категории</i>.

Если цена товара в юанях меньше 200 - 500р
Если больше 1000 юаней  - 2000руб
Если больше 1500 юаней  - 2500р
Если больше 2000 юаней  - 3000р

Курс: меняется каждый день, для уточнения курса свяжитесь с менеджером @getpoizon_manager
                               '''
    message_reviews = '''
                    ⭐️Отзывы

Здесь все отзывы, которые оставили клиенты, кто заказывал через телеграм: https://t.me/poizonget

Большая часть отзывов на авито: https://www.avito.ru/user/640af7bb44be68239d05095eef17bd33/profile?src=sharing
                               '''
    message_instruction = '''
    🌍 Инструкция по POIZON 

https://youtu.be/CDZ99F9sqoA
                               '''
    message_partner = '''
⭕️ Оптовые заказы и сотрудничество с нами
    
Каждый случай рассматривается индивидуально, всё зависит от объёмов и частоты заказов.
Опт идёт от 5 пар.

Пишите: @Getpoizon_manager
                                   '''

    message_chet = """
Итого {0}₽ без учёта доставки до Москвы.\n 
<b>СТОИМОСТЬ ТОВАРА ПРИМЕРНАЯ, ТОЧНАЯ ЦЕНА УЗНАЁТСЯ У МЕНЕДЖЕРА ПРИ ЗАКАЗЕ</b>"""
