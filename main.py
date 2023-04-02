from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from config import BOT_TOKEN
import keyboard
from states import Start

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


curs = 12.9


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await bot.send_message(message.from_user.id,
                           text=(
                               'Добро пожаловать в Get Poison'), reply_markup=keyboard)


@dp.message_handler(commands=["Рассчитать стоимость"], state="*")
async def rasshet(message: types.Message):
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await bot.send_message(message.from_user.id,
                           text=(
                               'Добро пожаловать в Get Poison. Введите стоимость '))
    await Start.schet.set()

@dp.message_handler(state=Start.schet)
async def rasshet_itog (message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['stoim'] = message.text
        stoim_cny = int( data['stoim'])
        itog = stoim_cny * curs + 1500
        await bot.send_message(message.from_user.id,
                            text=(
                                'Сумма вашего заказа  = ' + str (itog)))
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
