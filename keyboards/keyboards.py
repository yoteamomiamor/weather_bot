from aiogram.types import (InlineKeyboardButton, 
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from fluentogram import TranslatorRunner

from keyboards.callback_factory import WeatherCallback


def get_main_keyboard(lang: TranslatorRunner) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=lang.get_weather()),
            KeyboardButton(text=lang.set_location())
            ]],
        resize_keyboard=True,
        input_field_placeholder=lang.select_placeholder()
    )


def get_location_keyboard(lang: TranslatorRunner) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=lang.send_location(), request_location=True),
            KeyboardButton(text=lang.cancel())
        ]],
        resize_keyboard=True,
        input_field_placeholder=lang.select_placeholder()
    )


def get_weather_keyboard(lang: TranslatorRunner) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text=lang.weather_today(), 
                callback_data=WeatherCallback(date=0, days=1).pack()
            ),
            InlineKeyboardButton(
                text=lang.weather_tomorrow(),
                callback_data=WeatherCallback(date=1, days=1).pack()
            ),
            InlineKeyboardButton(
                text=lang.weather_week(),
                callback_data=WeatherCallback(date=0, days=7).pack()
            )
        ]]
    )