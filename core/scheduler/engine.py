from aiogram import Bot

from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator

from core.utils.configer import bot, redis_data


async_scheduler = ContextSchedulerDecorator(AsyncIOScheduler(
        timezone="Europe/Kiev",
        jobstores={
            'default': RedisJobStore(
                jobs_key='dispatched_trips_jobs',
                run_times_key='dispatched_trips_running',
                db=redis_data['redis_name'],
                host=redis_data['redis_host'],
                port=redis_data['redis_port'],
            )
        }
    )
)

async_scheduler.ctx.add_instance(bot, declared_class=Bot)
