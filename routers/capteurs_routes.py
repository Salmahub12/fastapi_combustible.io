from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Capteur
from schemas import CapteurCreate, Capteur as CapteurSchema
from database import *



capteur_router = APIRouter()

#Acces en lecture
@capteur_router.get("/capteurs/{capteur_id}")
def read_capteur(capteur_id: int, db: Session = Depends(get_db)):
    capteur = db.query(Capteur).filter(Capteur.ID_Capteur == capteur_id).first()
    if capteur is None:
        raise HTTPException(status_code=404, detail="Capteur not found")
    return capteur

@capteur_router.get("/capteurs")
def read_all_capteurs(db: Session = Depends(get_db)):
    capteurs = db.query(Capteur).all()
    if capteurs is None:
        raise HTTPException(status_code=404, detail="Capteurs not found")
    return capteurs

#Acces en écriture (créer une nouvelle instance de l'objet)
@capteur_router.post("/capteurs", response_model=CapteurSchema)
def create_capteur(capteur: CapteurCreate, db: Session = Depends(get_db)):
    db_capteur = Capteur(**capteur.model_dump())
    db.add(db_capteur)
    db.commit()
    db.refresh(db_capteur)
    return db_capteur

#Acces en écriture (modification de la velur d'une donnée de l'objet)
@capteur_router.put("/cateurs/{capteurs_id}", response_model=CapteurSchema)
def update_capteur(capteur_id: int, updated_capteur: CapteurCreate, db: Session = Depends(get_db)):
    capteur = db.query(Capteur).filter(Capteur.ID_Capteur == capteur_id).first()
    
    if capteur is None:
        raise HTTPException(status_code=404, detail="Capteur not found")
    
    for key, value in updated_capteur.model_dump().items():
        setattr(capteur, key, value)

    db.commit()
    db.refresh(capteur)
    
    return capteur

#Suppression
@capteur_router.delete("/capteurs/{capteurs_id}")
def delete_capteur(capteur_id: int, db: Session = Depends(get_db)):
    capteur = db.query(Capteur).filter(Capteur.ID_Capteur == capteur_id).first()

    if capteur is None:
        raise HTTPException(status_code=404, detail="Capteur not found")
    
    db.delete(capteur)
    db.commit()
    db.refresh(capteur)

    return {"message": "Capteurs successfully deleted"}
    



