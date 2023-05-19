
from fastapi import FastAPI,Depends
import schemas
from database import engine,SessionLocal
import model
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

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

@app.get('/users',tags=['user'])
async def qr(db : Session = Depends(get_db)):
    
    user1 = db.query(model.user).all()
    return user1

