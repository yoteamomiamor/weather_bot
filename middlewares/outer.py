from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from fluentogram import TranslatorHub

from typing import Dict, Callable, Awaitable, Any, Union


class TranslatorMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        
        hub: TranslatorHub = data.get('_translator_hub')
        lang = event.from_user.language_code
        data['lang'] = hub.get_translator_by_locale(lang)
        
        return await handler(event, data)
