from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class keyboard(ReplyKeyboardMarkup):
    kb_start = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True, row_width=2)
    b1_start = KeyboardButton("Расcчитать стоимость")
    b2_start = KeyboardButton("Полезные ссылки")
    b3_start = KeyboardButton("Заказать")
    b4_start = KeyboardButton("Помощь")
    kb_start.add(b1_start, b2_start, b3_start, b4_start)
