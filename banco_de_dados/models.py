from sqlalchemy import Boolean, Column, Integer, String
from banco_de_dados.database import Base

#Criação da tabela usuário com auntenticação JWT
class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(255))


#Criação da tabela posts.
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)