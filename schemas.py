from pydantic import BaseModel


class User(BaseModel):
    Name:str
    password:str
    email:str