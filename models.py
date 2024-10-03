from sqlalchemy import DATE, DATETIME, DECIMAL, VARCHAR, Column, ForeignKey, Integer, Date
from database import Base

class Capteur(Base):
    __tablename__ = "Capteurs"

    ID_Capteur = Column(Integer, primary_key=True, nullable=False)
    Date_Installation = Column(Date, nullable=False)
    Type_Donnees = Column(Integer, ForeignKey('Type_Donnees.ID_Type'), nullable=False)
    ID_Reservoir = Column(Integer, ForeignKey('Reservoir.ID_Reservoir'), nullable=False)
    Date_Fin = Column(Date, nullable=True)  # Permettre des dates de fin nulles


class Centrale(Base):
    __tablename__ = "Centrale"

    ID_Centrale = Column(Integer, primary_key=True, nullable=False)
    Nom = Column(VARCHAR(50), nullable=False)
    Chef_Centrale = Column(Integer, ForeignKey('Utilisateurs.ID_Utilisateur'), nullable=False)
    Coordonnee_x = Column(DECIMAL(18,0), nullable=False)
    Coordonnee_y = Column(DECIMAL(18,0), nullable=False)


class DonneesCapteur(Base):
    __tablename__ = "Donnees_Capteurs"

    ID_Donnee = Column(Integer, primary_key=True, nullable=False)
    Date_Heure = Column(DATETIME, nullable=False)
    ID_Reservoir = Column(Integer, ForeignKey('Reservoir.ID_Reservoir'), nullable=False)
    ID_Capteur = Column(Integer, ForeignKey('Capteurs.ID_Capteur'), nullable=False)
    Valeur = Column(DECIMAL(18,0), nullable=False)


class Reservoir(Base):
    __tablename__ = "Reservoir"

    ID_Reservoir = Column(Integer, primary_key=True, nullable=False, autoincrement=False)
    Capacite_Totale = Column(Integer, nullable=False)
    ID_Centrale = Column(Integer, ForeignKey('Centrale.ID_Centrale'), nullable=False)
    Combustible = Column(VARCHAR(255), nullable=False)


class Seuils(Base):
    __tablename__ = "Seuils"

    ID_Reservoir = Column(Integer, ForeignKey('Reservoir.ID_Reservoir'), primary_key=True, nullable=False)
    Niveau_Haut = Column(VARCHAR(50), nullable=True)
    Niveau_Bas = Column(VARCHAR(50), nullable=True)
    Date_Debut = Column(DATE, nullable=True)
    Date_Fin = Column(DATE, nullable=True)


class TypeDonnees(Base):
    __tablename__ = "Type_Donnees"

    ID_Type = Column(Integer, primary_key=True, nullable=False)
    Description_Donnees = Column(VARCHAR(255), nullable=True)


class Utilisateurs(Base):
    __tablename__ = "Utilisateurs"

    ID_Utilisateur = Column(Integer, primary_key=True, nullable=False)
    Nom = Column(VARCHAR(50), nullable=True)
    Prenom = Column(VARCHAR(50), nullable=True)
    Email = Column(VARCHAR(50), nullable=True)
    Mdp = Column(VARCHAR(50), nullable=True)
    Fonction = Column(VARCHAR(50), nullable=True)
