from fastapi import FastAPI , Depends , HTTPException 
from database import create_db,get_session , select 
from models import User
from sqlalchemy.ext.asyncio import AsyncSession 
from schemas import Usercreate

async def lifespan(app:FastAPI):
    await create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/get_users")
async def get_all_users(db:AsyncSession=Depends(get_session)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@app.post("/create_user")
async def create_user(user:Usercreate,db:AsyncSession=Depends(get_session)):
    new_user = User(name=user.name,age=user.age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.get("/get_user/{username}")
async def get_user(username:str,db:AsyncSession=Depends(get_session)):
    user = await db.execute(select(User).where(User.name == username))
    user = user.scalars().all()
    return user

@app.post("/update_user/{username}")
async def update_user(username:str,update:str,db:AsyncSession=Depends(get_session)):
    user = await db.execute(select(User).where(User.name == username))
    user = user.scalar_one_or_none()
    user.name = update
    await db.commit()
    await db.refresh(user)
    return user