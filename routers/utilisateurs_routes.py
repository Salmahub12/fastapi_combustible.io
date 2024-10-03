from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Utilisateurs
from schemas import UtilisateursCreate, Utilisateurs as UtilisateurSchema
from database import *



utilisateur_router = APIRouter()


@utilisateur_router.get("/utilisateur/{utilisateur_id}")
def read_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateurs).filter(Utilisateurs.ID_Capteur == utilisateur_id).first()
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur

@utilisateur_router.get("/utilisateurs")
def read_all_utilisateurs(db: Session = Depends(get_db)):
    utilisateurs = db.query(Utilisateurs).all()
    if utilisateurs is None:
        raise HTTPException(status_code=404, detail="Utilisateurs not found")
    return utilisateurs

#Acces en écriture(créer une nouvelle instance de l'objet)
@utilisateur_router.post("/utilisateurs", response_model=UtilisateurSchema)
def create_utilisateur(utilisateur: UtilisateursCreate, db: Session = Depends(get_db)):
    db_utilisateur = Utilisateurs(**utilisateur.model_dump())
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur

#Acces en écriture(modification de la valeur d'une donnee)
@utilisateur_router.put("/utilisateur/{utilisateur_id}", response_model=UtilisateurSchema)
def update_utilisateur(utilisateur_id: int, updated_utilisateur: UtilisateursCreate, db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateurs).filter(Utilisateurs.ID_Utilisateur == utilisateur_id).first()
    
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Type Donnees not found")
    
    for key, value in updated_utilisateur.model_dump().items():
        setattr(utilisateur, key, value)

    db.commit()
    db.refresh(utilisateur)
    
    return utilisateur

#Suppression
@utilisateur_router.delete("/utilisateur/{utilisateur_id}")
def delete_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateurs).filter(Utilisateurs.ID_Type == utilisateur_id).first()

    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    
    db.delete(utilisateur)
    db.commit()
    db.refresh(utilisateur)

    return {"message": "Utilisateur successfully deleted"}
