from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from config import BOT_TOKEN
from keyboard import inlinekeyboard, Rasschet_Keyboard
from states import Start
from checker import checker

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


curs = 12.9
nacenka1 = 500
nacenka2 = 1000
nacenka3 = 2000
nacenka4 = 2500
nacenka5 = 3000
dostavka = 1300


@dp.callback_query_handler(text="main")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_photo(callback.from_user.id, open('src/img/Shapka.jpg', "rb"),
                         f"""
🤠Нихао, Что можем сделать для тебя?
                               """, reply_markup=inlinekeyboard.inline_start, parse_mode=types.ParseMode.HTML)


@ dp.message_handler(commands=["start"])
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await message.answer_photo(open('src/img/Shapka.jpg', "rb"),
                               f"""
🤠 Нихао, {firstname}!
Добро пожаловать в нашу команду GET POIZON

Что сделать для тебя?
                               """, reply_markup=inlinekeyboard.inline_start, parse_mode=types.ParseMode.HTML)


@ dp.message_handler(lambda message: message.text == "Связаться с оператором")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
<b>Готов оформить заказ или есть вопросы?</b>

Напиши нашему менеджеру @Getpoizon_manager

""", parse_mode=types.ParseMode.HTML)


@ dp.message_handler(lambda message: message.text == "Заказать")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
<b>Готов оформить заказ или есть вопросы?</b>

Напиши нашему менеджеру @Getpoizon_manager

""", parse_mode=types.ParseMode.HTML)


@ dp.message_handler(lambda message: message.text == "Почему нам можно доверять?")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
<b>Готов оформить заказ или есть вопросы?</b>

Напиши нашему менеджеру @Getpoizon_manager

""", parse_mode=types.ParseMode.HTML)

# @dp.message_handler(lambda message: message.text == "Сделать заказ", state="*")
# async def rasshet_itog(message: types.Message):
#     await message.answer("Ок")


@ dp.callback_query_handler(text="calculate")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_photo(callback.from_user.id, open('src/img/Shapka.jpg', "rb"),
                         caption=(
        ''' 
Введите цену на товар в <b>ЮАНЯХ</b>🇨🇳
и бот покажет цену с учётом доставки до склада в Москве
Внимание! Выбирайте цену, которая <b>ЗАЧЕРКНУТА</b> и находится <b>СЛЕВА</b>.
Система отображает скидки для первых покупателей. 

<b>У нас нет этих скидок!</b> 

                               '''), parse_mode=types.ParseMode.HTML)
    await Start.schet.set()


@dp.callback_query_handler(text="order")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''
                    💎 Оформить заказ. 

Для заказа свяжитесь с менеджером, предоставьте фото товара и укажите ваш размер.

@Getpoizon_manager

                               '''), parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="scum")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''
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

                               '''), parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="course")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''
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

                               '''), parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="reviews")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''
                    ⭐️Отзывы

Здесь все отзывы, которые оставили клиенты, кто заказывал через телеграм: https://t.me/poizonget

Большая часть отзывов на авито: https://www.avito.ru/user/640af7bb44be68239d05095eef17bd33/profile?src=sharing
                               '''), parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="instruction")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''
    🌍 Инструкция по POIZON 

https://youtu.be/CDZ99F9sqoA
                               '''), parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="commission")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''
    🌚 Наша комиссия, курс 

Комиссия❇️
Рассчитывается <i>каждому индивидуально</i>, потому что комиссия зависит от <i>цены товара</i> и от <i>категории</i>.
Если цена товара в юанях меньше 200 - 500р
Если больше 1000 юаней  - 2000руб
Если больше 1500 юаней  - 2500р
Если больше 2000 юаней  - 3000р

Курс: меняется каждый день, для уточнения курса свяжитесь с менеджером @getpoizon_manager
                               '''), parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="partner")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    # await message.edit_text("Так")

    await bot.send_message(callback.from_user.id,
                           text=(
                               '''

    ⭕️ Оптовые заказы и сотрудничество с нами

    Каждый случай рассматривается индивидуально, всё зависит от объёмов и частоты заказов.
    Опт идёт от 5 пар.

    Пишите: @Getpoizon_manager
                                   '''), parse_mode=types.ParseMode.HTML)


@dp.message_handler(state=Start.schet)
async def rasshet_itog(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['stoim'] = message.text
        stoim = data['stoim']
        s = ''
        stoim_cny, s = await checker(stoim, s)
        if stoim_cny == -1:
            await bot.send_message(message.from_user.id,
                                   text=s)
            await Start.schet.set()
        else:
            if stoim_cny <= 200:
                itog = stoim_cny * curs + nacenka1
            elif stoim_cny <= 1000:
                itog = stoim_cny * curs + nacenka2
            elif stoim_cny <= 1500:
                itog = stoim_cny * curs + nacenka3
            elif stoim_cny <= 2000:
                itog = stoim_cny * curs + nacenka4
            else:
                itog = stoim_cny * curs + nacenka5
            await bot.send_message(message.from_user.id,
                                   text=(
                                       f"""
                                       Итого {str(round(itog))}₽ без учёта доставки до Москвы.\n 
<b>СТОИМОСТЬ ТОВАРА ПРИМЕРНАЯ, ТОЧНАЯ ЦЕНА УЗНАЁТСЯ У МЕНЕДЖЕРА ПРИ ЗАКАЗЕ</b>"""), reply_markup=Rasschet_Keyboard.inline_rasschet, parse_mode=types.ParseMode.HTML)
            await state.finish()


@dp.message_handler(content_types=['text'])
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Ок")

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
