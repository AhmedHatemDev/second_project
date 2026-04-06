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

class User(Base):
    __tablename__ = 'users'
    id = Column(String,primary_key=True,default=lambda:str(uuid4()))
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)

async def create_db():
    async with engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)

async def get_session():
    async with loaclsession() as session:
        yield session