from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot) -> None:
    commands = [
        BotCommand(command='start', description='go to the main menu'),
        BotCommand(command='help', description='get info about bot'),
        BotCommand(command='where', description='shows your set location'),
        BotCommand(command='location', description='set a new location'),
        BotCommand(command='cancel', description='cancel setting location')
    ]
    await bot.set_my_commands(
        commands=commands
    )
