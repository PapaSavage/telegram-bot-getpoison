from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


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


class inlinekeyboard(InlineKeyboardMarkup):
    inline_start = InlineKeyboardMarkup(resize_keyboard=True,
                                        one_time_keyboard=True, row_width=2)
    inline_b1_start = InlineKeyboardButton(
        "Кулькулятор цены", callback_data='calculate')
    inline_b2_start = InlineKeyboardButton(
        "💎Оформить заказ", callback_data='order')
    inline_b3_start = InlineKeyboardButton("Про скам🙈", callback_data='scum')
    inline_b4_start = InlineKeyboardButton(
        "Про курс 💹", callback_data='course')
    inline_b5_start = InlineKeyboardButton("⭐️Отзывы", callback_data='reviews')
    inline_b6_start = InlineKeyboardButton(
        "🌍 Инструкция по POIZON", callback_data='instruction', row=1)
    inline_b7_start = InlineKeyboardButton(
        "🌚 Наша комиссия, курс", callback_data='commission', row=1)
    inline_b8_start = InlineKeyboardButton(
        "⭕️ Оптовые заказы и сотрудничество с нами", callback_data='partner', row=1)
    inline_start.add(inline_b1_start, inline_b2_start, inline_b3_start,
                     inline_b4_start, inline_b5_start, inline_b6_start, inline_b7_start, inline_b8_start)


class Rasschet_Keyboard(InlineKeyboardMarkup):
    inline_rasschet = InlineKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True, row_width=2)
    inline_b1_rasschet = InlineKeyboardButton(
        "Ещё расчёт!🔄", callback_data='calculate')
    inline_b2_rasschet = InlineKeyboardButton(
        "Заказать!👑", callback_data='order')
    inline_b3_rasschet = InlineKeyboardButton("Главная", callback_data='main')
    inline_rasschet.add(inline_b1_rasschet,
                        inline_b2_rasschet, inline_b3_rasschet)
