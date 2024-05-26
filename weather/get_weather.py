import aiohttp
import json
from typing import Any
from weather.sourcetemplate import sourcetemplate
from aiogram_i18n import I18nContext
import pandas as pd
import logging

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
    date_slice = slice(start, end)
    df = pd.DataFrame(data).iloc[1:]
    weather_code = most_common(df.loc['weather_code'].hourly[date_slice])
    df.hourly = df.hourly.apply(lambda S: avg(S[date_slice]))

    df = df[['hourly_units', 'hourly']]
    df = df.apply(lambda S: f"{S.hourly}{S.hourly_units}", axis=1)
    df.loc['weather_code'] = weather_code
    
    if end - start == 24:
        time_interval = i18n.date_from_now(day=start // 24)
    else:
        time_interval = f'{start % 24}:00 - {end % 24}:00'
    
    return i18n.weather_by_hours(time_interval=time_interval, **df.to_dict())


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

