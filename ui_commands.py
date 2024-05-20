from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot) -> None:
    commands = [
        BotCommand(command='help', description='get info about bot'),
        BotCommand(command='cancel', description='cancel setting location')
    ]
    await bot.set_my_commands(
        commands=commands
    )
