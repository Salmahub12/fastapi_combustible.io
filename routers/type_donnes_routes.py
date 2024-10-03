from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import TypeDonnees
from schemas import TypeCreate, Type as TypeSchema
from database import *



type_router = APIRouter()


#Acces en lecture
@type_router.get("/type/{type_id}")
def read_type(type_id: int, db: Session = Depends(get_db)):
    type = db.query(TypeDonnees).filter(TypeDonnees.ID_Capteur == type_id).first()
    if type is None:
        raise HTTPException(status_code=404, detail="Type de donnees not found")
    return type

@type_router.get("/types")
def read_all_types(db: Session = Depends(get_db)):
    types = db.query(TypeDonnees).all()
    if types is None:
        raise HTTPException(status_code=404, detail="Types not found")
    return types

#Acces en écriture(créer une nouvelle instance de l'objet)
@type_router.post("/Type_Donnees", response_model=TypeSchema)
def create_type(type: TypeCreate, db: Session = Depends(get_db)):
    db_type = TypeDonnees(**type.model_dump())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type


#Acces en écriture(modification de la valeur d'une donnée)
@type_router.put("/type/{type_id}", response_model=TypeSchema)
def update_type(type_id: int, updated_type: TypeCreate, db: Session = Depends(get_db)):
    type = db.query(TypeDonnees).filter(TypeDonnees.ID_Type == type_id).first()
    
    if type is None:
        raise HTTPException(status_code=404, detail="Type Donnees not found")
    
    for key, value in updated_type.model_dump().items():
        setattr(type, key, value)

    db.commit()
    db.refresh(type)
    
    return type

#Suppression
@type_router.delete("/type/{type_id}")
def delete_type(type_id: int, db: Session = Depends(get_db)):
    type = db.query(TypeDonnees).filter(TypeDonnees.ID_Type == type_id).first()

    if type is None:
        raise HTTPException(status_code=404, detail="Type Donnees not found")
    
    db.delete(type)
    db.commit()
    db.refresh(type)

    return {"message": "Type Donnees successfully deleted"}