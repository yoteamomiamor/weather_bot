from aiogram.filters.callback_data import CallbackData


class WeatherCallback(CallbackData):
    date: int
    days: int
