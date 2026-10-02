from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Marque(Base):
    __tablename__ = 'Marque'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Modele(Base):
    __tablename__ = 'Modele'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    ID_Marque = Column(Integer, ForeignKey('Marque.id'))
    def __init__(self,row,mapping_marque):
        self.name=row.Modele
        self.ID_Marque=mapping_marque[row.Marque]
    
class Energie(Base):
    __tablename__ = 'Energie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class BoiteVitesse(Base):
    __tablename__ = 'BoiteVitesse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    
class Type(Base):
    __tablename__ = 'Type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    
class Voiture(Base):
    __tablename__ = 'Voiture'
    ID_Voiture = Column(Integer, primary_key=True, autoincrement=True)
    Prix = Column(Float)
    PrixNeuf = Column(Float)
    Kilometre = Column(Integer)
    Annee = Column(Integer)
    Chevaux = Column(Integer)
    
    ID_Type = Column(Integer, ForeignKey('Type.id'))
    ID_Marque = Column(Integer, ForeignKey('Marque.id'))
    ID_Modele = Column(Integer, ForeignKey('Modele.id'))
    ID_Energie = Column(Integer, ForeignKey('Energie.id'))
    ID_BoiteVitesse = Column(Integer, ForeignKey('BoiteVitesse.id'))
    
    bluetooth=Column(Integer)
    cam_recul=Column(Integer)
    clim_auto=Column(Integer)
    feux_led=Column(Integer)
    gps=Column(Integer)
    inte_cuir=Column(Integer)
    isofix=Column(Integer)
    jantes_alliage=Column(Integer)
    radar_recul=Column(Integer)
    regulateur_vitesse=Column(Integer)
    tete_haute=Column(Integer)
    toit_ouvrant=Column(Integer)
    toit_panoramique=Column(Integer)
    trois_siege_indiv=Column(Integer)
    def __init__(self,row,mapping_btv,mapping_model,mapping_energie, mapping_marque, mapping_type):
        self.Kilometre=row.Kilometre
        self.Prix=row.Prix
        self.PrixNeuf=row.Prix
        self.Annee=row.Annee
        self.Chevaux=row.Chevaux
        
        #options
        self.bluetooth=row.bluetooth
        self.cam_recul=row.cam_recul
        self.clim_auto=row.clim_auto
        self.feux_led=row.feux_led
        self.gps=row.gps
        self.inte_cuir=row.inte_cuir
        self.isofix=row.isofix
        self.jantes_alliage=row.jantes_alliage
        self.radar_recul=row.radar_recul
        self.regulateur_vitesse=row.regulateur_vitesse
        self.tete_haute=row.tete_haute
        self.toit_ouvrant=row.toit_ouvrant
        self.toit_panoramique=row.toit_panoramique
        self.trois_siege_indiv=row.trois_siege_indiv
        
        self.ID_Type=mapping_type[row.type]
        self.ID_Marque=mapping_marque[row.Marque]
        self.ID_Energie=mapping_energie[row.Energie]
        self.ID_Modele=mapping_model[row.Modele]
        self.ID_BoiteVitesse=mapping_btv[row[["Boites de vitesse"]].values[0]]
        pass
