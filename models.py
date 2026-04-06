from sqlalchemy import Column , String , Integer
from database import Base
from uuid import uuid4

class User(Base):
    __tablename__ = 'users'
    id = Column(String,primary_key=True,default=lambda:str(uuid4()))
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)