from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


class StartKeyboard(ReplyKeyboardMarkup):
    kb_start = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True, row_width=2)
    b1_start = KeyboardButton("Главная")

    kb_start.add(b1_start)


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


class ToMain(InlineKeyboardMarkup):
    inline_main = InlineKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True)

    inline = InlineKeyboardButton("Главная", callback_data='main')
    inline_main.add(inline)


class AdminKeyboard(InlineKeyboardMarkup):
    inline_Admin = InlineKeyboardMarkup(resize_keyboard=True,
                                        one_time_keyboard=True, row_width=2)

    inline_calc = InlineKeyboardButton(
        "Смена данных для рассчёта", callback_data='ARasschet')
    inline_message = InlineKeyboardButton(
        "Смена текста сообщений", callback_data='AMessages')
    inline_Admin.add(inline_calc, inline_message)


class ARasschet(InlineKeyboardMarkup):
    inline_perechet = InlineKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True, row_width=1)

    curs = InlineKeyboardButton(
        "Смена данных для рассчёта", callback_data='ОбъявлениеКурса')
    nacenka1 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара меньше 200 юаней", callback_data='Объявление наценки 1')
    nacenka2 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 500 юаней", callback_data='Объявление наценки 2')
    nacenka3 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 1000 юаней", callback_data='Объявление наценки 3')
    nacenka4 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 1500 юаней", callback_data='Объявление наценки 4')
    nacenka5 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 2000 юаней", callback_data='Объявление наценки 5')
    # dostavka = InlineKeyboardButton(
    #     "Смена текста сообщений", callback_data='Доставка')
    inline_perechet.add(curs, nacenka1, nacenka2, nacenka3,
                        nacenka4, nacenka5)
