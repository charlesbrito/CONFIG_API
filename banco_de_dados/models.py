from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from banco_de_dados.database import Base
from sqlalchemy.orm import relationship

#Criação da tabela usuário com auntenticação JWT
class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    post = relationship("Post", back_populates="user", uselist=False)


#Criação da tabela posts.
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    user = relationship("User", back_populates="post")