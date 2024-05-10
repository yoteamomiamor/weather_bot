import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from configs import Config, load_config
from handlers import common
from middlewares import outer

from locales.get_hub import get_hub

import logging


logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('starting bot')

    config: Config = load_config()

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp = Dispatcher()

    dp.include_routers(common.rt)
    
    dp.message.middleware(outer.TranslatorMiddleware())

    # await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=get_hub(config.languages))


if __name__ == '__main__':
    asyncio.run(main())
