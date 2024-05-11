from aiogram.filters.callback_data import CallbackData


class WeatherCallback(CallbackData, prefix='weather_date'):
    date: int
    days: int
