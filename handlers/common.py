from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from fluentogram import TranslatorRunner


rt = Router()


@rt.message(CommandStart())
async def process_start_command(message: Message, lang: TranslatorRunner):
    name = message.from_user.full_name
    await message.answer(text=lang.start(name=name))


@rt.message(Command('help'))
async def process_help_command(message: Message, lang: TranslatorRunner):
    await message.answer(text=lang.help())
