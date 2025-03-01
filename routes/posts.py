from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from banco_de_dados import models
from banco_de_dados.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from JWT import auth
from JWT.auth import get_current_user

router = APIRouter()
router.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='A autenticação falhou')
    return {"user": user}

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

# Endpoint para criar posts
@router.post("/posts/", tags=["post"], status_code=status.HTTP_201_CREATED)
async def criar_post(post: PostBase, db:db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    
    

   