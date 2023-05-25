from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship

class user(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True,index = True,autoincrement=True)
    name=Column(String) 
    email=Column(String) 
    password=Column(String)
    points = Column(Integer,default=0)
    uid = Column(String)
    role = Column(String,default="user")
    
class Product(Base):
    __tablename__ = "product"

    pid = Column(Integer, index=True, primary_key=True)
    pname = Column(String)
    ppid = Column(String, nullable=True)
    puechaserd = Column(Boolean, default=False)

class purchase(Base):  
    __tablename__ = "purchase info"

    id = Column(Integer,index = True,primary_key = True)
    pname=Column(String) 
    pid = Column(String, nullable = True,primary_key = True)
    puechaserd = Column(Boolean,default=False)
    uid = Column(String, nullable = True)
    uname = Column(String)
    