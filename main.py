from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from config import BOT_TOKEN
from keyboard import keyboard
from states import Start
from checker import checker

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


curs = 12.9
nacenka = 1500
dostavka = 1300

@dp.message_handler(commands=["start"], state="*")
async def start_command(message: types.Message):
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await message.answer_photo(message.from_user.id,
                               text=(open("src/img/Shapka.jpg", "rb"),
                                     f"""
🤠 Нихао, {firstname}!
Мы прямые посредники Poizon.
У нас свой склад в Китае, поэтому мы можем давать минимальную цену🔥
И ещё очень много плюшек!
Контакт для связи: @Getpoizon_manager

<b><i>❗️Только оригинальная продукция</i></b>
                               """), reply_markup=keyboard.kb_start, parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: message.text == "Связаться с оператором", state="*")
async def rasshet_itog(message: types.Message):
    await message.answer(f"""
*Готов оформить заказ или есть вопросы?*                        

Напиши нашему менеджеру @Getpoizon_manager

При 
                         """, parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(lambda message: message.text == "Сделать заказ", state="*")
async def rasshet_itog(message: types.Message):
    await message.answer("Ок")


@dp.message_handler(lambda message: message.text == "Расcчитать стоимость", state="*")
async def rasshet(message: types.Message):
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await bot.send_message(message.from_user.id,
                           text=(
                               'Добро пожаловать в Get Poison. Введите стоимость '))
    await Start.schet.set()


@dp.message_handler(state=Start.schet)
async def rasshet_itog(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['stoim'] = message.text
        stoim = data['stoim']
        s = ''
        stoim_cny,s = await checker(stoim, s)
        if stoim_cny == -1:
            await bot.send_message(message.from_user.id,
                               text=(s))
            await Start.schet.set()    
        else:                       
            itog = stoim_cny * curs + nacenka + dostavka
            await bot.send_message(message.from_user.id,
                                text=(
                                    'Сумма вашего заказа  = ' + str(itog)))
            await state.finish()

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
