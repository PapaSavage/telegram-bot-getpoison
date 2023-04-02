from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class keyboard(ReplyKeyboardMarkup):
    kb_start = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True, row_width=2)
    b1_start = KeyboardButton("Расcчитать стоимость")
    b2_start = KeyboardButton("Полезные ссылки")
    b3_start = KeyboardButton("Заказать")
    b4_start = KeyboardButton("Помощь")
    b5_start = KeyboardButton("Связаться с оператором")
    b6_start = KeyboardButton("Почему нам можно доверять?")
    kb_start.add(b1_start, b2_start, b3_start,
                 b4_start, b5_start, b6_start)
