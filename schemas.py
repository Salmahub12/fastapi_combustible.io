from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal

# Capteur Schemas
class CapteurBase(BaseModel):
    Date_Installation: date
    Type_Donnees: int
    ID_Reservoir: int
    Date_Fin: Optional[date] = None

    class Config:
        from_attributes = True

class CapteurCreate(CapteurBase):
    pass

class Capteur(CapteurBase):
    ID_Capteur: int

   

# Centrale Schemas
class CentraleBase(BaseModel):
    Nom: str
    Chef_Centrale: int
    Coordonnee_x: Decimal
    Coordonnee_y: Decimal

    class Config:
        from_attributes = True


class CentraleCreate(CentraleBase):
    pass

class Centrale(CentraleBase):
    ID_Centrale: int

#Nom Centrale Schemas
class NomCentraleResponse(BaseModel):
    nom_centrale: str

    class Config:
        from_attributes = True


# Données Capteur Schemas
class DonneesBase(BaseModel):
    Date_Heure: datetime
    ID_Reservoir: int
    ID_Capteur: int
    Valeur: Decimal

class DonneesCreate(DonneesBase):
    pass 

class DonneesCapteur(DonneesBase):
    ID_Donnee: int

    class Config:
        from_attributes = True

# Reservoir Schemas
class ReservoirBase(BaseModel):
    ID_Reservoir: int
    Capacite_Totale: int
    ID_Centrale: int
    Combustible: str

class ReservoirCreate(ReservoirBase):
    pass

class Reservoir(ReservoirBase):
   class Config: 
        from_attributes = True

#Count reservoir

class CountResponse(BaseModel):
    count: int

# Seuils Schemas
class SeuilsBase(BaseModel):
    ID_Reservoir: int
    Niveau_Haut: str
    Niveau_Bas: str
    Date_Debut: date
    Date_Fin: Optional[date] = None

class SeuilsCreate(SeuilsBase):
    pass

class Seuils(SeuilsBase):
    class Config:
        from_attributes = True

# Type de Données Schemas
class TypeBase(BaseModel):
    Description_Donnees: str

class TypeCreate(TypeBase):
    pass

class Type(TypeBase):
    ID_Type: int

    class Config:
        from_attributes = True

# Utilisateurs Schemas
class UtilisateursBase(BaseModel):
    Nom: str
    Prenom: str
    Email: str
    Mdp: str
    Fonction: str

class UtilisateursCreate(UtilisateursBase):
    pass

class Utilisateurs(UtilisateursBase):
    ID_Utilisateur: int

    class Config:
        from_attributes = True

class UtilisateurLogin(BaseModel):
    Email: str
    Mdp: str
