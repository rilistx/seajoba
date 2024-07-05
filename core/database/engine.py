from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.settings import postgres_url


# Here we create async engine for the PostgreSQL database
async_engine = create_async_engine(
    url=postgres_url,
    echo=True,
)

# Here we create async session for the PostgreSQL database
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
