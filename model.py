from pydantic import BaseModel , Field
from uuid import uuid4

class Usercreate(BaseModel):
    name:str
    age:int