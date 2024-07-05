__all__ = [
    'bot',
    'storage',
    'admin_id',
    'forum_id',
    'premium_id',
    'postgres_url',
]


from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from core.settings.envs import my_envs


bot_token = my_envs.get_bot_token()
pay_token = my_envs.get_pay_token()

admin_id = my_envs.get_admin_id()
forum_id = my_envs.get_forum_id()

premium_id = my_envs.get_premium_id()

postgres_data = my_envs.get_postgres_data()
redis_data = my_envs.get_redis_data()

postgres_url = 'postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}/{pg_name}'.format(**postgres_data)
redis_url = 'redis://{redis_host}:{redis_port}/{redis_name}'.format(**redis_data)

parse_mode = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token=bot_token, default=parse_mode)
storage = RedisStorage.from_url(url=redis_url)
