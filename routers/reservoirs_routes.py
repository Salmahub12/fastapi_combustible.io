from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Reservoir
from schemas import ReservoirCreate, Reservoir as ReservoirSchema
from schemas import CountResponse as CountSchema
from database import *



reservoir_router = APIRouter()


#Acces en lecture
@reservoir_router.get("/reservoir/{reservoir_id}")
def read_reservoir(reservoir_id: int, db: Session = Depends(get_db)):
    reservoir = db.query(Reservoir).filter(Reservoir.ID_Reservoir == reservoir_id).first()
    if reservoir is None:
        raise HTTPException(status_code=404, detail="Reservoir not found")
    return reservoir

@reservoir_router.get("/reservoirs")
def read_all_capteurs(db: Session = Depends(get_db)):
    reservoirs = db.query(Reservoir).all()
    if reservoirs is None:
        raise HTTPException(status_code=404, detail="Reservoirs not found")
    return reservoirs


#Acces en écriture(créer une nouvelle instance de l'objet)
@reservoir_router.post("/reservoir", response_model=ReservoirSchema)
def create_reservoir(reservoir: ReservoirCreate, db: Session = Depends(get_db)):
    db_reservoir = Reservoir(**reservoir.model_dump())
    db.add(db_reservoir)
    db.commit()
    db.refresh(db_reservoir)
    return db_reservoir

#Acces en écriture(modification de la valeur d'une donnée)
@reservoir_router.put("/reservoir/{reservoir_id}", response_model=ReservoirSchema)
def update_reservoir(reservoir_id: int, updated_reservoir: ReservoirCreate, db: Session = Depends(get_db)):
    reservoir = db.query(Reservoir).filter(Reservoir.ID_Reservoir == reservoir_id).first()
    
    if reservoir is None:
        raise HTTPException(status_code=404, detail="Reservoir not found")
    
    for key, value in updated_reservoir.model_dump().items():
        setattr(reservoir, key, value)

    db.commit()
    db.refresh(reservoir)
    
    return reservoir

#Suppression
@reservoir_router.delete("/reservoir/{reservoir_id}")
def delete_reservoir(reservoir_id: int, db: Session = Depends(get_db)):
    reservoir = db.query(Reservoir).filter(Reservoir.ID_Reservoir == reservoir_id).first()

    if reservoir is None:
        raise HTTPException(status_code=404, detail="Reservoir not found")
    
    db.delete(reservoir)
    db.commit()
    db.refresh(reservoir)

    return {"message": "Reservoir successfully deleted"}

# Nombre de réservoirs 
@reservoir_router.get("/reservoirs/count", response_model=CountSchema)
def nombre_reservoir(db: Session = Depends(get_db)):
    count = db.query(Reservoir).count()  # Query the count of rows in the Reservoir table
    return CountSchema(count=count)