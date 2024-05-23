import aiohttp
import json
from typing import Any
from weather.sourcetemplate import sourcetemplate
from aiogram_i18n import I18nContext
from datetime import datetime


url = 'https://api.open-meteo.com/v1/forecast'
get_query = sourcetemplate(url)


async def _get_weather(query: str) -> dict[str, Any]:
    """Makes weather request asynchronously"""
    async with aiohttp.ClientSession() as session:
        async with session.get(query) as response:
            return json.loads(await response.text())


async def get_current_weather(i18n: I18nContext, **params) -> str:
    arguments = {
        'latitude': params['latitude'],
        'longitude': params['longitude'],
        'current': ['temperature_2m', 'precipitation', 'weather_code']
    }
    
    data = await _get_weather(get_query(**arguments))
    units = data['current_units']
    current = data['current']

    return i18n.current_weather_info(
        temperature=current['temperature_2m'],
        unit_temperature=units['temperature_2m'],
        precipitation=current['precipitation'],
        unit_precipitation=units['precipitation'],
        weather_code=current['weather_code']
    )


async def get_today_weather(i18n: I18nContext, **params) -> str:
    return 'today\'s weather is good'


async def get_tomorrow_weather(i18n: I18nContext) -> str:
    return 'tomorrow\'s weather is good'


async def get_week_weather(i18n: I18nContext) -> str:
    return 'weekly weather is good'
