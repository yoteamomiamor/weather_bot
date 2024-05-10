from environs import Env
from dataclasses import dataclass
from typing import Optional


@dataclass
class Bot:
    token: str
    

@dataclass
class Config:
    bot: Bot


def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(Bot(env('BOT_TOKEN')))
