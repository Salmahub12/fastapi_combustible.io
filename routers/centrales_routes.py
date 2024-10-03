from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Centrale
from schemas import CentraleCreate, Centrale as CentraleSchema
from schemas import NomCentraleResponse as NomSchema
from database import *



centrale_router = APIRouter()

#Acces en lecture
@centrale_router.get("/centrale/{centrale_id}")
def read_centrale(centrale_id: int, db: Session = Depends(get_db)):
    centrale = db.query(Centrale).filter(Centrale.ID_Centrale == centrale_id).first()
    if centrale is None:
        raise HTTPException(status_code=404, detail="Centrale not found")
    return centrale

@centrale_router.get("/centrale")
def read_all_centrales(db: Session = Depends(get_db)):
    centrale = db.query(Centrale).all()
    if centrale is None:
        raise HTTPException(status_code=404, detail="Centrale not found")
    return centrale

#Accès en écriture (créer une nouvelle instance)
@centrale_router.post("/centrale", response_model=CentraleSchema)
def create_centrale(centrale: CentraleCreate, db: Session = Depends(get_db)):
    db_centrale = Centrale(**centrale.model_dump())
    db.add(db_centrale)
    db.commit()
    db.refresh(db_centrale)
    return db_centrale

#Acces en écriture (modifier la valeur d'une donnée)
@centrale_router.put("/centrale/{centrale_id}", response_model=CentraleSchema)
def update_centrale(centrale_id: int, updated_centrale: CentraleCreate, db: Session = Depends(get_db)):
    centrale = db.query(Centrale).filter(Centrale.ID_Centrale == centrale_id).first()
    
    if centrale is None:
        raise HTTPException(status_code=404, detail="Centrale not found")
    
    for key, value in updated_centrale.model_dump().items():
        setattr(centrale, key, value)

    db.commit()
    db.refresh(centrale)

    return centrale

#Supression 
@centrale_router.delete("/centrale/{centrale_id}")
def delete_centrale(centrale_id: int, db: Session = Depends(get_db)):
    centrale = db.query(Centrale).filter(Centrale.ID_Centrale == centrale_id).first()

    if centrale is None:
        raise HTTPException(status_code=404, detail="Centrale not found")
    
    db.delete(centrale)
    db.commit()
    db.refresh(centrale)

    return {"message": "Cantrale successfully deleted"}

#Avoir le nom de la Centrale
@centrale_router.get("/centrale/{centrale_id}/nom", response_model=NomSchema)
def get_nom_centrale(centrale_id: int, db: Session = Depends(get_db)):
    centrale = db.query(Centrale).filter(Centrale.ID_Centrale == centrale_id).first()

    if not centrale:
        raise HTTPException(status_code=404, detail="Centrale not found")
    
    return {"nom_centrale" : centrale.Nom}

 