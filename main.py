from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from config import BOT_TOKEN


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await bot.send_message(message.from_user.id,
                           text=(
                               'Добро пожаловать'))


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
