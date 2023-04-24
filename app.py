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
nacenka = 1000
dostavka = 1300


@dp.message_handler(commands=["start"], state="*")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await message.answer_photo(open('src/img/Shapka.jpg', "rb"),
                               f"""
🤠 Нихао, {firstname}!
Добро пожаловать в нашу команду GET POIZON

Что сделать для тебя?"
                               """, reply_markup=inlinekeyboard.inline_start, parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: message.text == "Связаться с оператором", state="*")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
<b>Готов оформить заказ или есть вопросы?</b>                        

Напиши нашему менеджеру @Getpoizon_manager
 
""", parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: message.text == "Заказать", state="*")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
<b>Готов оформить заказ или есть вопросы?</b>                        

Напиши нашему менеджеру @Getpoizon_manager
 
""", parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: message.text == "Почему нам можно доверять?", state="*")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
<b>Готов оформить заказ или есть вопросы?</b>                        

Напиши нашему менеджеру @Getpoizon_manager
 
""", parse_mode=types.ParseMode.HTML)

# @dp.message_handler(lambda message: message.text == "Сделать заказ", state="*")
# async def rasshet_itog(message: types.Message):
#     await message.answer("Ок")


@dp.callback_query_handler(text="calculate", state="*")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_photo(user_id, open('src/img/Shapka.jpg', "rb"),
                         caption=(
        ''' 
Введите цену на товар в <b>ЮАНЯХ</b>🇨🇳
и бот покажет цену с учётом доставки до склада в Москве
Внимание! Выбирайте цену, которая <b>ЗАЧЕРКНУТА</b> и находится <b>СЛЕВА</b>.
Система отображает скидки для первых покупателей. 

<b>У нас нет этих скидок!</b> 

                               '''), parse_mode=types.ParseMode.HTML)
    await Start.schet.set()


@dp.callback_query_handler(text="btn1", state="*")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.send_photo(user_id, open('src/img/Shapka.jpg', "rb"),
                         caption=(
        ''' 
Введите цену на товар в <b>ЮАНЯХ</b>🇨🇳
и бот покажет цену с учётом доставки до склада в Москве
Внимание! Выбирайте цену, которая <b>ЗАЧЕРКНУТА</b> и находится <b>СЛЕВА</b>.
Система отображает скидки для первых покупателей. 

<b>У нас нет этих скидок!</b> 

                               '''), parse_mode=types.ParseMode.HTML)
    await Start.schet.set()


@dp.message_handler(state=Start.schet)
async def rasshet_itog(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['stoim'] = message.text
        stoim = data['stoim']
        s = ''
        stoim_cny, s = await checker(stoim, s)
        if stoim_cny == -1:
            await bot.send_message(message.from_user.id,
                                   text=(s))
            await Start.schet.set()
        else:
            itog = stoim_cny * curs + nacenka + dostavka
            await bot.send_message(message.from_user.id,
                                   text=(
                                       f"""
                                       Итоговая стоимость: {str(round(itog))}₽\n
Стоимость включает: 
Курс ¥ - {str(curs)}₽
Доставка  {str(dostavka)}₽
Комиссия нашего сервиса - {str(nacenka)}₽"""), reply_markup=Rasschet_Keyboard.inline_rasschet)
            await state.finish()


@dp.message_handler(content_types=['text'])
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Ок")

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
