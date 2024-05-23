from environs import Env
from dataclasses import dataclass
from typing import Optional
from os.path import join


@dataclass
class Bot:
    token: str
    

@dataclass
class Config:
    bot: Bot
    languages: str
    db_url: str


def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=Bot(env('BOT_TOKEN')),
        languages=(join('.', 'locales', 'languages')),
        db_url=env('DB_URL')
    )
