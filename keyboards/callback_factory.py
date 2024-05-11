from aiogram.filters.callback_data import CallbackData


class WeatherCallback(CallbackData):
    days: int
