import aiohttp
import json
from typing import Any
from weather.sourcetemplate import sourcetemplate
from aiogram_i18n import I18nContext
import logging
from datetime import datetime
from pprint import pprint

logger = logging.getLogger(f'__main__.{__name__}')


url = 'https://api.open-meteo.com/v1/forecast'
get_query = sourcetemplate(url)


def avg(seq: list | tuple) -> int:
    """Returns rounded average number of the sequence"""
    return round(sum(seq) / len(seq))


def most_common(L: list) -> Any:
    """Returns most common value from a list"""
    freq_dict = {}.fromkeys(L, 0)
    max_value = 0
    max_key = 0
    for key in L:
        freq_dict[key] += 1
        if freq_dict[key] > max_value:
            max_value = freq_dict[key]
            max_key = key
    return max_key


async def _get_weather(query: str) -> dict[str, Any]:
    """Makes weather request asynchronously"""
    async with aiohttp.ClientSession() as session:
        async with session.get(query) as response:
            return json.loads(await response.text())


def weather_by_hours(i18n: I18nContext,
                     data: dict[str, Any],
                     start: int = 0, 
                     end: int = 24) -> str:
    """
    Gets weather description by given time.
    The default time values are the minimum
    and maximum
    """
    weather_type = 'hourly'
    weather = data[weather_type]
    units = data[weather_type + '_units']

    weather_data = {}
    for key in weather:
        if key == 'time':
            time = datetime.fromisoformat(weather[key][start])
            weekday = i18n.weekday(day=time.weekday())
            month = i18n.months(month=time.month)
            if end - start == 24:
                weather_data[key] = f'{time:{weekday}, %d {month} %Y}'
            else:
                weather_data[key] = (f'{start%24}:00 - {end%24}:00  |  '
                                     f'{time:{weekday}, %d {month} %Y}')
        elif key == 'weather_code':
            weather_data[key] = most_common(weather[key][start:end])
        else:
            weather_data[key] = f'{avg(weather[key][start:end])}{units[key]}'

    return i18n.weather_by_hours(**weather_data)


async def get_current_weather(i18n: I18nContext, **params) -> str:
    request_params = {
        'latitude': params['latitude'],
        'longitude': params['longitude'],
        'current': ['temperature_2m', 'precipitation', 'weather_code']
    }
    
    data = await _get_weather(get_query(**request_params))

    return i18n.current_weather_info(
        **{key: value for key, value in data['current'].items()}
    )


async def get_today_weather(i18n: I18nContext, **params) -> str:
    request_params = {
        'latitude': params['latitude'],
        'longitude': params['longitude'],
        'hourly': [
            'temperature_2m',
            'relative_humidity_2m',
            'apparent_temperature',
            'precipitation_probability',
            'precipitation',
            'weather_code',
            'cloud_cover',
            'visibility',
            'wind_speed_10m'
            ],
        'forecast_days': 1
    }
    
    data = await _get_weather(get_query(**request_params))
    return (i18n.one_day_weather(day_name='today') + '\n' +
            '\n'.join(
                [weather_by_hours(i18n, data, start=i, end=i+6)
                 for i in range(0, 24, 6)]
            )
    )


async def get_tomorrow_weather(i18n: I18nContext, **params) -> str:
    request_params = {
        'latitude': params['latitude'],
        'longitude': params['longitude'],
        'hourly': [
            'temperature_2m',
            'relative_humidity_2m',
            'apparent_temperature',
            'precipitation_probability',
            'precipitation',
            'weather_code',
            'cloud_cover',
            'visibility',
            'wind_speed_10m'
            ],
        'forecast_days': 2
    }
    
    data = await _get_weather(get_query(**request_params))
    return (i18n.one_day_weather(day_name='tomorrow') + '\n' +
            '\n'.join(
                [weather_by_hours(i18n, data, i, i+6)
                 for i in range(24, 48, 6)]
            )
    )


async def get_week_weather(i18n: I18nContext, **params) -> str:
    request_params = {
        'latitude': params['latitude'],
        'longitude': params['longitude'],
        'hourly': [
            'temperature_2m',
            'relative_humidity_2m',
            'apparent_temperature',
            'precipitation_probability',
            'precipitation',
            'weather_code',
            'cloud_cover',
            'visibility',
            'wind_speed_10m'
            ],
        'forecast_days': 7
    }
    
    data = await _get_weather(get_query(**request_params))
    return (i18n.week_weather() + '\n' +
            '\n'.join(
                [weather_by_hours(i18n, data, i, i+24)
                 for i in range(0, 24*7, 24)]
            )
    )

