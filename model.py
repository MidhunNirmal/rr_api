from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class user(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True,index = True)
    name=Column(String) 
    email=Column(String) 
    password=Column(String)
    # qr = Column(LargeBinary, nullable = True)
    