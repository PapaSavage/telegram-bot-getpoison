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
                                        one_time_keyboard=True, row_width=1)

    inline_calc = InlineKeyboardButton(
        "Смена данных для рассчёта", callback_data='ARasschet')
    inline_message = InlineKeyboardButton(
        "Смена текста сообщений", callback_data='AMessages')
    inline = InlineKeyboardButton("Главная", callback_data='main')
    inline_Admin.add(inline_calc, inline_message, inline)


class ARasschet(InlineKeyboardMarkup):
    inline_perechet = InlineKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True, row_width=1)

    curs = InlineKeyboardButton(
        "Смена курса", callback_data='ОбъявлениеКурса')
    nacenka1 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара меньше 200 юаней", callback_data='ОбъявлениеНаценки1')
    nacenka2 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 500 юаней", callback_data='ОбъявлениеНаценки2')
    nacenka3 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 1000 юаней", callback_data='ОбъявлениеНаценки3')
    nacenka4 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 1500 юаней", callback_data='ОбъявлениеНаценки4')
    nacenka5 = InlineKeyboardButton(
        "Пересмотр наценки стоимости товара больше 2000 юаней", callback_data='ОбъявлениеНаценки5')
    # dostavka = InlineKeyboardButton(
    #     "Смена текста сообщений", callback_data='Доставка')
    inline_perechet.add(curs, nacenka1, nacenka2, nacenka3,
                        nacenka4, nacenka5)
class AMessages(InlineKeyboardMarkup):
    inline_messages = InlineKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=True, row_width=1)

    message_hello = InlineKeyboardButton(
        "Смена текста приветственного сообщения", callback_data='Приветственное сообщение')
    message_rasschet = InlineKeyboardButton(
        "Смена текста сообщения перед расчетом", callback_data='Сообщение перед расчетом')
    message_order = InlineKeyboardButton(
        "Смена текста оформить заказ", callback_data='Оформить заказ')
    message_scum = InlineKeyboardButton(
        "Смена текста про скам ", callback_data='Скам')
    message_course = InlineKeyboardButton(
        "Смена текста про курс", callback_data='Курс')
    message_commission = InlineKeyboardButton(
        "Смена текста наша комиссия", callback_data='Комиссия')
    message_reviews = InlineKeyboardButton(
        "Смена текста отзывы", callback_data='Отзывы')
    message_instruction = InlineKeyboardButton(
        "Смена текста инструкция ", callback_data='Инструкция')
    message_partner = InlineKeyboardButton(
        "Смена текста оптовые заказы и сотрудничество с нами", callback_data='Сотрудничество')
    message_chet = InlineKeyboardButton(
        "Смена текста выводимого при расчете", callback_data='Расчет')
    inline_messages.add(message_hello, message_rasschet,message_order,message_scum,message_course,
                        message_commission,message_reviews,message_instruction,message_partner,message_chet)
