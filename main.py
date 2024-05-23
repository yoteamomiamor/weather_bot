import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.i18n import I18n, ConstI18nMiddleware

from aiogram_i18n import I18nContext, I18nMiddleware, LazyProxy
from aiogram_i18n.cores import FluentRuntimeCore

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from configs import Config, load_config
from handlers import common, weather_handlers
from ui_commands import set_main_menu
from middlewares.db import DBSessionMiddleware

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

    engine = create_async_engine(config.db_url, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="locales/{locale}")
    )
    
    dp = Dispatcher()

    dp.update.middleware(DBSessionMiddleware(session_pool=sessionmaker))
    i18n_middleware.setup(dispatcher=dp)
    
    dp.include_routers(common.rt, weather_handlers.rt)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
