from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    Name:str
    password:str
    email:str
class User(BaseModel):
    Name:str
    password:str
    email:str
class login(BaseModel):
    Name:str
    password:str
    
class UserInDB(User):
    password: str    

    
class Token(BaseModel):
    access_token: str
    token_type: str


# class TokenData(BaseModel):
#     name: str | None = None

class TokenData(BaseModel):
    name: Union[str, None] = None

    