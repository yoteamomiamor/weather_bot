from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext, LazyProxy

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.models import User

from weather.get_weather import (get_today_weather,
                                 get_tomorrow_weather,
                                 get_week_weather)
from handlers.states import MainFSM

from typing import Callable
from logging import getLogger


rt = Router()


logger = getLogger(__name__)


async def request_weather(message: Message, session: AsyncSession, 
                          i18n: I18nContext, weather_getter: Callable):
    user_id = message.from_user.id
    sql_query = (select(User.lat, User.long)
                 .where(User.user_id == user_id)
                 .limit(1))
    data = await session.execute(sql_query)
    data = data.first()
    if not data:
        return i18n.no_set_location()
    
    lat, long = data
    await session.commit()
    
    return await weather_getter(
            i18n=i18n, 
            latitude=lat, 
            longitude=long
        )

# today
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_today'))
async def process_today_button(message: Message, state: FSMContext,
                               i18n: I18nContext, session: AsyncSession):
    await message.answer(
        text=await request_weather(message, session, i18n, get_today_weather)
    )
    
    
# tomorrow
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_tomorrow'))
async def process_tomorrow_button(message: Message, state: FSMContext,
                               i18n: I18nContext, session: AsyncSession):
    await message.answer(
        text=await request_weather(message, session, i18n, get_tomorrow_weather)
    )

# week
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_week'))
async def process_week_button(message: Message, state: FSMContext,
                               i18n: I18nContext, session: AsyncSession):
    await message.answer(
        text=await request_weather(message, session, i18n, get_week_weather)
    )
