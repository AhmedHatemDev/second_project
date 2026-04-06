from sqlalchemy.ext.asyncio import create_async_engine , AsyncSession,async_sessionmaker
from collections.abc import AsyncGenerator
from sqlalchemy.orm import sessionmaker , DeclarativeBase
from sqlalchemy import Column , Integer , String , UUID , select
from uuid import uuid4
import asyncio

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL)
loaclsession = async_sessionmaker(engine,expire_on_commit=False)
class Base(DeclarativeBase):
    pass

async def create_db():
    async with engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)

async def get_session():
    async with loaclsession() as session:
        yield session