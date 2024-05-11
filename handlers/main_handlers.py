from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from fluentogram import TranslatorRunner

from keyboards.keyboards import (get_main_keyboard, get_location_keyboard,
                                 get_weather_keyboard)
from weather.get_weather import today_weather
from handlers.FSMStates import FSMMain


rt = Router()


@rt.message(Command('location'), default_state)
@rt.message(F.text == 'location', default_state)
async def process_settings_command(message: Message, state: FSMContext,
                                   lang: TranslatorRunner):
    await state.set_state(FSMMain.add_location)
    await message.answer(
        text=lang.wait_location(),
        reply_markup=get_location_keyboard(lang)
    )


@rt.message(Command('weather'), default_state)
@rt.message(F.text == 'weather', default_state)
async def process_weather_command(message: Message, state: FSMContext,
                                 lang: TranslatorRunner):
    await state.set_state(FSMMain.select_weather)
    await message.answer(
        text=lang.select_weather(),
        reply_markup=get_weather_keyboard(lang)
    )
