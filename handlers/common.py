from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext, LazyProxy

from keyboards.keyboards import get_main_keyboard, get_weather_keyboard
from handlers.states import MainFSM
from weather.get_weather import get_current_weather


rt = Router()


@rt.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext,
                                i18n: I18nContext):
    name = message.from_user.full_name
    await state.set_state(MainFSM.menu)
    await message.answer(
        text=i18n.start(name=name),
        reply_markup=get_main_keyboard(i18n)
    )


@rt.message(Command('help'))
async def process_help_command(message: Message, i18n: I18nContext):
    await message.answer(text=i18n.help())


@rt.message(Command('cancel'))
@rt.message(F.text == LazyProxy('cancel'))
async def process_cancel_command(message: Message, state: FSMContext,
                                 i18n: I18nContext):
    await state.set_state(MainFSM.menu)
    await message.answer(
        text=i18n.main(),
        reply_markup=get_main_keyboard(i18n)
    )


@rt.message(F.text == LazyProxy('get_weather'))
async def process_weather_button(message: Message, state: FSMContext,
                                 i18n: I18nContext):
    await state.set_state(MainFSM.select_weather)
    await message.answer(
        text=i18n.select_weather(),
        reply_markup=get_weather_keyboard(i18n)
    )


@rt.message(F.location)
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
