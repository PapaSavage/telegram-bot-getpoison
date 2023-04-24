from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from config import BOT_TOKEN
from keyboard import inlinekeyboard, Rasschet_Keyboard, ToMain, StartKeyboard, ARasschet, AdminKeyboard
from states import Start
from checker import checker
from admin import Admin
from contextlib import suppress
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


# Каждое отправление сообщения теперь надо записать в переменную g = bot.send и прочие
# Example - prev_message.append()


async def delete_message(message: types.Message, seconds: int = 0):
    Admin.prev_message.append(message)
    if len(Admin.prev_message) > 1:
        message = Admin.prev_message[0]
        await bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=None)
        Admin.prev_message.pop(0)
    # await asyncio.sleep(seconds)

    # await bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=None)

    seconds += 900

    await asyncio.sleep(seconds)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


@dp.callback_query_handler(text="main")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=inlinekeyboard.inline_start)

#     await bot.send_photo(callback.from_user.id, open('src/img/Shapka.jpg', "rb"),
#                          f"""
# 🤠Нихао, Что можем сделать для тебя?
#                                """, reply_markup=inlinekeyboard.inline_start, parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await message.answer_photo(open('src/img/Shapka.jpg', "rb"),
                               Admin.message_hello.format(firstname), reply_markup=inlinekeyboard.inline_start, parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: message.text == "Главная")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    global user_id
    user_id = message.from_user.id
    firstname = message.from_user.first_name
    await message.answer_photo(open('src/img/Shapka.jpg', "rb"),
                               Admin.message_hello.format(firstname), reply_markup=inlinekeyboard.inline_start, parse_mode=types.ParseMode.HTML)


@ dp.callback_query_handler(text="calculate")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):
    message = await bot.send_photo(callback.from_user.id, open('src/img/Shapka.jpg', "rb"),
                                   caption=(Admin.message_rasschet), parse_mode=types.ParseMode.HTML)
    await Start.schet.set()
    await asyncio.create_task(await delete_message(message, 3600))


@dp.callback_query_handler(text="order")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_order), reply_markup=ToMain.inline_main, parse_mode=types.ParseMode.HTML)
    await delete_message(message, 3600)


@dp.callback_query_handler(text="scum")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_scum), reply_markup=ToMain.inline_main,  parse_mode=types.ParseMode.HTML)
    await delete_message(message, 60)


@dp.callback_query_handler(text="course")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_course), reply_markup=ToMain.inline_main, parse_mode=types.ParseMode.HTML)

    await delete_message(message, 60)


@dp.callback_query_handler(text="reviews")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_reviews), reply_markup=ToMain.inline_main, parse_mode=types.ParseMode.HTML)
    # await asyncio.create_task(await delete_message(message, 60))
    await delete_message(message, 60)


@dp.callback_query_handler(text="instruction")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_instruction), reply_markup=ToMain.inline_main, parse_mode=types.ParseMode.HTML)

    await delete_message(message, 60)


@dp.callback_query_handler(text="commission")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_commission), reply_markup=ToMain.inline_main, parse_mode=types.ParseMode.HTML)
    await delete_message(message, 60)


@dp.callback_query_handler(text="partner")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    # await message.edit_text("Так")

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         Admin.message_partner), reply_markup=ToMain.inline_main, parse_mode=types.ParseMode.HTML)

    await delete_message(message, 60)


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
                itog = stoim_cny * Admin.curs + Admin.nacenka1
            elif stoim_cny <= 1000:
                itog = stoim_cny * Admin.curs + Admin.nacenka2
            elif stoim_cny <= 1500:
                itog = stoim_cny * Admin.curs + Admin.nacenka3
            elif stoim_cny <= 2000:
                itog = stoim_cny * Admin.curs + Admin.nacenka4
            else:
                itog = stoim_cny * Admin.curs + Admin.nacenka5
            message = await bot.send_message(message.from_user.id,
                                             text=(
                                                 Admin.message_chet.format(str(round(itog)))), reply_markup=Rasschet_Keyboard.inline_rasschet, parse_mode=types.ParseMode.HTML)
            await delete_message(message, 60)
            await state.finish()


@dp.message_handler(content_types=['text'])
async def fault(message: types.Message, state: FSMContext):
    fault = await message.answer("Выберите кнопку из предложенных)")
    await asyncio.sleep(25)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await fault.delete()


@dp.callback_query_handler(text="Admin", state="*")
async def adminka(callback: types.CallbackQuery, state=FSMContext):
    bot.send_message(callback.from_user.id, """Приветствую вас в настройках бота
                     Выберите то, что хотите отредактировать""", reply_markup=AdminKeyboard.inline_Admin, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="ARasschet")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         "Выберите действие"), reply_markup=ARasschet.inline_perechet, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="ОбъявлениеКурса")
async def rasshet(callback: types.CallbackQuery, state=FSMContext):

    message = await bot.send_message(callback.from_user.id,
                                     text=(
                                         "Выберите действие"), reply_markup=ARasschet.inline_perechet, parse_mode=types.ParseMode.HTML)


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
