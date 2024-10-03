from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Seuils
from schemas import SeuilsCreate, Seuils as SeuilsSchema
from database import *



seuil_router = APIRouter()


#Acces en lecture
@seuil_router.get("/seuil/{seuil_id}")
def read_seuil(seuil_id: int, db: Session = Depends(get_db)):
    seuil = db.query(Seuils).filter(Seuils.ID_Reservoir == seuil_id).first()
    if seuil is None:
        raise HTTPException(status_code=404, detail="Seuil not found")
    return seuil

@seuil_router.get("/seuils")
def read_all_seuils(db: Session = Depends(get_db)):
    seuils = db.query(Seuils).all()
    if seuils is None:
        raise HTTPException(status_code=404, detail="Seuils not found")
    return seuils

#Acces en écriture(créer une nouvelle instance de l'objet)
@seuil_router.post("/seuils", response_model=SeuilsSchema)
def create_seuil(seuil: SeuilsCreate, db: Session = Depends(get_db)):
    db_seuil = Seuils(**seuil.model_dump())
    db.add(db_seuil)
    db.commit()
    db.refresh(db_seuil)
    return db_seuil


#Acces en écriture(modification de la valeur d'une donnée)
@seuil_router.put("/seuil/{seuil_id}", response_model=SeuilsSchema)
def update_seuil(seuil_id: int, updated_reservoir: SeuilsCreate, db: Session = Depends(get_db)):
    seuil = db.query(Seuils).filter(Seuils.ID_Reservoir == seuil_id).first()
    
    if seuil is None:
        raise HTTPException(status_code=404, detail="Seuil not found")
    
    for key, value in updated_reservoir.model_dump().items():
        setattr(seuil, key, value)

    db.commit()
    db.refresh(seuil)
    
    return seuil

#Suppression
@seuil_router.delete("/seuil/{seuil_id}")
def delete_seuil(seuil_id: int, db: Session = Depends(get_db)):
    seuil = db.query(Seuils).filter(Seuils.ID_Reservoir == seuil_id).first()

    if seuil is None:
        raise HTTPException(status_code=404, detail="Seuil not found")
    
    db.delete(seuil)
    db.commit()
    db.refresh(seuil)

    return {"message": "Seuil successfully deleted"}