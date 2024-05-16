from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext, LazyProxy

from weather.get_weather import *
from handlers.states import MainFSM


rt = Router()

# today
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_today'))
async def process_today_button(message: Message, state: FSMContext,
                               i18n: I18nContext):
    await message.answer(
        text=get_today_weather(i18n)
    )

# tomorrow
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_tomorrow'))
async def process_tomorrow_button(message: Message, state: FSMContext,
                               i18n: I18nContext):
    await message.answer(
        text=get_tomorrow_weather(i18n)
    )

# week
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_week'))
async def process_week_button(message: Message, state: FSMContext,
                               i18n: I18nContext):
    await message.answer(
        text=get_week_weather(i18n)
    )
