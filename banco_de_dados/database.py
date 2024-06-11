from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv(override=True)


URL_DATABASE = os.getenv("key_database")
if not URL_DATABASE:
    raise ValueError("A URL do banco de dados não foi encontrada na variável de ambiente 'key_database'.")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()