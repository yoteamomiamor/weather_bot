from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext, LazyProxy

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.models import User

from weather.get_weather import *
from handlers.states import MainFSM


rt = Router()

# today
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_today'))
async def process_today_button(message: Message, state: FSMContext,
                               i18n: I18nContext, session: AsyncSession):
    user_id = message.from_user.id
    sql_query = (select(User.lat, User.long)
                 .where(User.user_id == user_id)
                 .limit(1))
    data = await session.execute(sql_query)
    await session.commit()
    
    for row in data:
        await message.answer(
            text=await get_today_weather(
                i18n=i18n, 
                latitude=row.lat, 
                longitude=row.long
            )
        )

# tomorrow
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_tomorrow'))
async def process_tomorrow_button(message: Message, state: FSMContext,
                               i18n: I18nContext, session: AsyncSession):
    user_id = message.from_user.id
    sql_query = (select(User.lat, User.long)
                 .where(User.user_id == user_id)
                 .limit(1))
    data = await session.execute(sql_query)
    await session.commit()
    
    for row in data:
        await message.answer(
            text=await get_tomorrow_weather(
                i18n=i18n, 
                latitude=row.lat, 
                longitude=row.long
            )
        )

# week
@rt.message(MainFSM.select_weather, F.text == LazyProxy('weather_week'))
async def process_week_button(message: Message, state: FSMContext,
                               i18n: I18nContext, session: AsyncSession):
    user_id = message.from_user.id
    sql_query = (select(User.lat, User.long)
                 .where(User.user_id == user_id)
                 .limit(1))
    data = await session.execute(sql_query)
    await session.commit()
    
    for row in data:
        await message.answer(
            text=await get_week_weather(
                i18n=i18n, 
                latitude=row.lat, 
                longitude=row.long
            )
        )
