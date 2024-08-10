from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from core.utils.receiver import Receiver


my_receiver = Receiver()


bot_token = my_receiver.get_bot_token()
bot_admin = my_receiver.get_bot_admin()

postgres_data = my_receiver.get_postgres_data()
redis_data = my_receiver.get_redis_data()

postgres_url = 'postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}/{pg_name}'.format(**postgres_data)
redis_url = 'redis://{redis_host}:{redis_port}/{redis_name}'.format(**redis_data)

parse_mode = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token=bot_token, default=parse_mode)
storage = RedisStorage.from_url(url=redis_url)
