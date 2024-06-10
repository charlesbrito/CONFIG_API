from sqlalchemy import Boolean, Column, Integer, String
from database import base

#Criação da tabela usuário com auntenticação JWT
class User(base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(255))


#Criação da tabela posts.
class Post(base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)