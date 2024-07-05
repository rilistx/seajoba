from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.settings import postgres_url


async_engine = create_async_engine(
    url=postgres_url,
    echo=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
