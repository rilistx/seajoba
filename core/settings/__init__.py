__all__ = [
    'bot',
    'admin',
    'storage',
    'postgres_url',
]


from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from core.settings.envs import my_envs


# Here are the telegram configurations from TelegramEnvs
bot_token = my_envs.get_bot_token()
pay_token = my_envs.get_pay_token()

# Here's the admin and chat ids
admin = my_envs.get_admin_id()
forum = my_envs.get_forum_id()

# Here are the database configurations from Envs
postgres_data = my_envs.get_postgres_data()
redis_data = my_envs.get_redis_data()

# Database string urls
postgres_url = 'postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}/{pg_name}'.format(**postgres_data)
redis_url = 'redis://{redis_host}:{redis_port}/{redis_name}'.format(**redis_data)

# Initialize bot with default parse mode as HTML
parse_mode = DefaultBotProperties(parse_mode=ParseMode.HTML)

# Bot object initialisation
bot = Bot(token=bot_token, default=parse_mode)

# This is the redis storage for the dispatcher.
storage = RedisStorage.from_url(url=redis_url)
