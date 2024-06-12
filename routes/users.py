from fastapi import APIRouter, Depends, HTTPException, status
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


# Endpoint para ler usuário por nome e retornar nome e post
@router.get("/users/{username}", tags=["user"], status_code=status.HTTP_200_OK)
async def ler_usuario_por_nome_e_retorna_nome_e_post(username: str, db:db_dependency):
    user_post = db.query(models.User.username, models.Post.content).join(models.Post, models.User.id == models.Post.user_id).filter(models.User.username == username).first()
    if user_post is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    user_name, post_content = user_post
    return {
        "usuário:": user_name,
        "Post:": post_content if post_content else None
    }
                                