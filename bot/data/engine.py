from typing import Union
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return _create_async_engine(
        url=url,
        echo=False,
        pool_pre_ping=True,
        future=True
    )

# @DeprecationWarning
async def processed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    # ...


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(
        engine=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )