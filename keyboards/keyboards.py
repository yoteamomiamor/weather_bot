from aiogram_i18n.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keyboard(i18n) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=i18n.get_weather()),
            KeyboardButton(text=i18n.set_location(), request_location=True)
            ]],
        resize_keyboard=True,
        input_field_placeholder=i18n.main()
    )


def get_weather_keyboard(i18n) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=i18n.weather_today()),
                KeyboardButton(text=i18n.weather_tomorrow()),
                KeyboardButton(text=i18n.weather_week()),
                ],
            [
                KeyboardButton(text=i18n.cancel())
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder=i18n.select_weather()
    )
