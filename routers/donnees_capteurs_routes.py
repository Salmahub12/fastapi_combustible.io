from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import DonneesCapteur
from schemas import DonneesCreate, DonneesCapteur as DonneesSchema
from database import *



donnees_router = APIRouter()


#Acces en lecture
@donnees_router.get("/donnees/{capteur_id}")
def read_donnees(donnees_id: int, db: Session = Depends(get_db)):
    donnees = db.query(DonneesCapteur).filter(DonneesCapteur.ID_Donnee == donnees_id).first()
    if donnees is None:
        raise HTTPException(status_code=404, detail="Donnees not found")
    return donnees

#Acces en écriture(créer une nouvelle instance de l'objet)
@donnees_router.get("/donnees")
def read_all_donnees(db: Session = Depends(get_db)):
    donnees = db.query(DonneesCapteur).all()
    if donnees is None:
        raise HTTPException(status_code=404, detail="Donnees not found")
    return donnees

@donnees_router.post("/donnees", response_model=DonneesSchema)
def create_donnees(donnees: DonneesCreate, db: Session = Depends(get_db)):
    db_donnees = DonneesCapteur(**donnees.model_dump())
    db.add(db_donnees)
    db.commit()
    db.refresh(db_donnees)
    return db_donnees

#Acces en écriture(modification de la valeur d'une donnee)
@donnees_router.put("/donnees/{donnees_id}", response_model=DonneesSchema)
def update_donnees(donnees_id: int, updated_donnees: DonneesCreate, db: Session = Depends(get_db)):
    donnees = db.query(DonneesCapteur).filter(DonneesCapteur.ID_Capteur == donnees_id).first()
    
    if donnees is None:
        raise HTTPException(status_code=404, detail="Donnees not found")
    
    for key, value in updated_donnees.model_dump().items():
        setattr(donnees, key, value)

    db.commit()
    db.refresh(donnees)
    
    return donnees

#Suppression
@donnees_router.delete("/donnees/{donnees_id}")
def delete_donnees(donnees_id: int, db: Session = Depends(get_db)):
    donnees = db.query(DonneesCapteur).filter(DonneesCapteur.ID_Capteur == donnees_id).first()

    if donnees is None:
        raise HTTPException(status_code=404, detail="Donnee not found")
    
    db.delete(donnees)
    db.commit()
    db.refresh(donnees)

    return {"message": "Donnee successfully deleted"}
