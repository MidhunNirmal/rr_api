
from fastapi import FastAPI,Depends
import schemas
from database import engine,SessionLocal
import model
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import pyqrcode
import png
from sqlalchemy import desc

# Generate QR code



app = FastAPI()
model.Base.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/user',tags=['user'])
async def user(request:schemas.User,db : Session = Depends(get_db)):
    
    user = model.user(name = request.Name,email = request.email,password = request.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user
 

@app.get('/user/{id1}',tags=['user'])
async def user(id1:int,db : Session = Depends(get_db)):
    
    user = db.query(model.user).filter(model.user.id == id1).first()
    return user


@app.get('/users',tags=['user'])
async def user(db : Session = Depends(get_db)):
    
    user1 = db.query(model.user).all()
    return user1

@app.get('/qr_gen/{id1}',tags=['user'])
async def qr(id1:int,db : Session = Depends(get_db)):
    user = db.query(model.user).filter(model.user.id == id1).first()
    key = user.name
    code = pyqrcode.create(key)
    qr_data = code.png_as_base64_str(scale=5)

    
    return {'qrdata':qr_data}

@app.put('/pointincrement/{id1}',tags=['user'])
async def user(id1:int,db : Session = Depends(get_db)):
    
    user = db.query(model.user).filter(model.user.id == id1).first()
    user.points=user.points+10
    db.commit()
    return "updated 10 points"


@app.get('/user_leaderboadrd',tags=['user'])
async def user(db : Session = Depends(get_db)):
    
    users = db.query(model.user).order_by(desc(model.user.points)).all()
    return users

