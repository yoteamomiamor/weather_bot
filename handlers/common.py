from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from fluentogram import TranslatorRunner

from keyboards.keyboards import get_main_keyboard


rt = Router()


@rt.message(CommandStart())
async def process_start_command(message: Message, lang: TranslatorRunner):
    name = message.from_user.full_name
    await message.answer(
        text=lang.start(name=name),
        reply_markup=get_main_keyboard(lang)
    )


@rt.message(Command('help'))
async def process_help_command(message: Message, lang: TranslatorRunner):
    await message.answer(text=lang.help())


@rt.message(Command('cancel'), ~StateFilter(default_state))
async def process_cancel_command(message: Message, state: FSMContext, 
                                 lang: TranslatorRunner):
    await state.set_state(default_state)
    await message.answer(
        text=lang.settings(),
        reply_markup=get_main_keyboard(lang)
    )
