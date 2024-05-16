import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.i18n import I18n, ConstI18nMiddleware

from aiogram_i18n import I18nContext, I18nMiddleware, LazyProxy
from aiogram_i18n.cores import FluentRuntimeCore

from configs import Config, load_config
from handlers import common, weather_handlers


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
    
    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="locales/{locale}")
    )
    
    dp = Dispatcher()

    i18n_middleware.setup(dispatcher=dp)
    
    dp.include_routers(common.rt, weather_handlers.rt)

    # await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
