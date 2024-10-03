import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Utilisateurs
from schemas import UtilisateurLogin as LoginSchema
from database import *

login_router = APIRouter()

@login_router.post("/login", response_model=LoginSchema)
def login(user: LoginSchema, db: Session = Depends(get_db)):
    db_utilisateur = db.query(Utilisateurs).filter(Utilisateurs.Email == user.Email).first()

    if not db_utilisateur or not bcrypt.checkpw(user.Mdp.encode('utf-8'), db_utilisateur.Mdp.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful", "username": db_utilisateur.Email}
    
