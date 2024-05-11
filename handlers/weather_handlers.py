from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from fluentogram import TranslatorRunner

from weather.get_weather import today_weather, week_weather, tomorrow_weather
from handlers.FSMStates import FSMMain

from keyboards.callback_factory import WeatherCallback


rt = Router()

# today
@rt.callback_query(WeatherCallback.filter(F.date == 0), 
                   WeatherCallback.filter(F.days == 1),
                   FSMMain.select_weather)
async def process_today_callback(callback: CallbackQuery, bot: Bot, 
                                 lang: TranslatorRunner):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=today_weather(lang)
    )

# tomorrow
@rt.callback_query(WeatherCallback.filter(F.date == 1), 
                   WeatherCallback.filter(F.days == 1),
                   FSMMain.select_weather)
async def process_todmorrow_callback(callback: CallbackQuery, bot: Bot, 
                                 lang: TranslatorRunner):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=tomorrow_weather(lang)
    )

# week
@rt.callback_query(WeatherCallback.filter(F.date == 0), 
                   WeatherCallback.filter(F.days == 7),
                   FSMMain.select_weather)
async def process_week_callback(callback: CallbackQuery, bot: Bot, 
                                 lang: TranslatorRunner):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=week_weather(lang)
    )


@rt.callback_query()
async def process_any_callback(callback: CallbackQuery, lang: TranslatorRunner):
    callback.answer(text=lang.invalid_message())
