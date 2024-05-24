from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from aiogram_i18n import I18nContext, LazyProxy

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.keyboards import *
from handlers.states import MainFSM
from weather.get_weather import get_current_weather
from db.models import User


rt = Router()


@rt.message(StateFilter(default_state), CommandStart())
async def process_start_command(message: Message, state: FSMContext,
                                i18n: I18nContext):
    name = message.from_user.full_name
    await state.set_state(MainFSM.menu)
    await message.answer(
        text=i18n.start(name=name),
        reply_markup=get_main_keyboard(i18n)
    )


@rt.message(~StateFilter(default_state), Command('help'))
async def process_help_command(message: Message, i18n: I18nContext):
    await message.answer(text=i18n.help())


@rt.message(~StateFilter(default_state, MainFSM.menu), Command('cancel'))
@rt.message(~StateFilter(default_state, MainFSM.menu),
            F.text == LazyProxy('cancel'))
async def process_cancel_command(message: Message, state: FSMContext,
                                 i18n: I18nContext):
    await state.set_state(MainFSM.menu)
    await message.answer(
        text=i18n.main(),
        reply_markup=get_main_keyboard(i18n)
    )


@rt.message(StateFilter(MainFSM.menu), F.text == LazyProxy('get_weather'))
async def process_weather_button(message: Message, state: FSMContext,
                                 i18n: I18nContext):
    await state.set_state(MainFSM.select_weather)
    await message.answer(
        text=i18n.select_weather(),
        reply_markup=get_weather_keyboard(i18n)
    )


@rt.message(StateFilter(MainFSM.menu), Command('set_location'))
@rt.message(StateFilter(MainFSM.menu), F.text == LazyProxy('set_location'))
async def process_location_button(message: Message, state: FSMContext,
                                 i18n: I18nContext):
    await state.set_state(MainFSM.set_location)
    await message.answer(
        text=i18n.wait_location(),
        reply_markup=get_location_keyboard(i18n)
    )


@rt.message(StateFilter(MainFSM.set_location), F.location)
async def process_set_location(message: Message, state: FSMContext,
                                i18n: I18nContext, session: AsyncSession):
    await session.merge(User(
        user_id=message.from_user.id,
        lat=message.location.latitude,
        long=message.location.longitude
        ))
    await session.commit()
    
    await state.set_state(MainFSM.menu)
    location = message.location
    await message.answer(
        text=i18n.location_is_set(
            latitude=location.latitude,
            longitude=location.longitude
        ),
        reply_markup=get_main_keyboard(i18n)
    )


@rt.message(~StateFilter(default_state), F.location)
async def process_sent_location(message: Message, state: FSMContext,
                                i18n: I18nContext):
    await state.set_state(MainFSM.menu)
    await message.answer(
        text=await get_current_weather(
            i18n, 
            latitude=message.location.latitude,
            longitude=message.location.longitude
        )
    )


@rt.message(~StateFilter(default_state), Command('where'))
async def process_where_command(message: Message, i18n: I18nContext,
                                session: AsyncSession):
    user_id = message.from_user.id
    sql_query = (select(User.lat, User.long)
                 .where(User.user_id == user_id)
                 .limit(1))
    data = await session.execute(sql_query)
    await session.commit()

    for row in data:
        await message.answer(i18n.where(latitude=row.lat, longitude=row.long))
