from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as _orm

# URL de connexion à SQL Server (modifiez-la en fonction de votre configuration)
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://LectSIP:LectSIP@srv-bddomtech/IOT_Combustible?driver=ODBC+Driver+17+for+SQL+Server"

# Créer un moteur SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Créer une session
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal

# Base pour les modèles ORM
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[_orm.Session, Depends(get_db)]

