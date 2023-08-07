from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: URL) -> AsyncEngine:
    return _create_async_engine(
        url=url,
        echo=True,
        # encoding="utf-8", 
        pool_pre_ping=True
    )


async def processed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.connect() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(
        engine=engine,
        class_=AsyncSession
    )