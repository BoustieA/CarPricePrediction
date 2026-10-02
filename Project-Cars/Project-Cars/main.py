from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from Data.orm import Marque  # Importer la classe Marque depuis le fichier orm.py dans le répertoire Data
from Data.orm import Energie  # Importer la classe Energie depuis le fichier orm.py dans le répertoire Data
from Data.orm import BoiteVitesse  # Importer la classe BoiteVitesse depuis le fichier orm.py dans le répertoire Data
from Data.orm import Type
from Data.orm import Voiture
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Initialisation de l'application FastAPI
app = FastAPI()

# Configuration de la base de données SQLite
DATABASE_URL = "sqlite:///./Data/database.sqlite"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Marque.metadata.create_all(bind=engine)
Energie.metadata.create_all(bind=engine)
Type.metadata.create_all(bind=engine)
BoiteVitesse.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modèle Pydantic pour la création et la mise à jour de la marque
class MarqueIn(BaseModel):
    name: str

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route de test : Hello World
@app.get("/")
def read_root():
    return {"Use /docs for documentation"}

# Route pour récupérer toutes les données

@app.get("/energies")
def get_energies(db: Session = Depends(get_db)):
    energies = db.query(Energie).all()  # Utilisation du modèle Marque
    return {"energies": [energie.name for energie in energies]}

@app.get("/voitures")
def get_voitures(db: Session = Depends(get_db)):
    voitures = db.query(Voiture).all()  # Utilisation du modèle Marque
    return voitures#[voiture.name for voiture in voitures]}

@app.get("/types")
def get_types(db: Session = Depends(get_db)):
    types = db.query(Type).all()  # Utilisation du modèle Marque
    return {"types": [type.name for type in types]}

@app.get("/boites")
def get_boites(db: Session = Depends(get_db)):
    boites = db.query(BoiteVitesse).all()  # Utilisation du modèle Marque
    return {"boites": [boite.name for boite in boites]}

@app.get("/marques")
def get_marques(db: Session = Depends(get_db)):
    marques = db.query(Marque).all()  # Utilisation du modèle Marque
    return {"marques": [marque.name for marque in marques]}

# Route pour récupérer une marque par son nom
@app.get("/marques/{name}")
def get_marque(name: str, db: Session = Depends(get_db)):
    marque = db.query(Marque).filter(Marque.name.ilike(name)).first()  # Utilisation du modèle Marque
    
    if not marque:
        raise HTTPException(status_code=404, detail="Marque non trouvée")
    
    return {"marque": marque.name}

# Route pour créer une nouvelle marque
@app.post("/marques")
def create_marque(marque: MarqueIn, db: Session = Depends(get_db)):
    db_marque = db.query(Marque).filter(Marque.name == marque.name).first()  # Utilisation du modèle Marque
    if db_marque:
        raise HTTPException(status_code=400, detail="Marque déjà existante")
    
    db.add(Marque(name=marque.name))  # Utilisation du modèle Marque
    db.commit()
    db.refresh(db_marque)
    
    return {"message": f"Marque '{marque.name}' créée avec succès"}

# Route pour mettre à jour une marque
@app.put("/marques/{name}")
def update_marque(name: str, marque: MarqueIn, db: Session = Depends(get_db)):
    db_marque = db.query(Marque).filter(Marque.name == name).first()  # Utilisation du modèle Marque
    if not db_marque:
        raise HTTPException(status_code=404, detail="Marque non trouvée")
    
    db_marque.name = marque.name
    db.commit()
    db.refresh(db_marque)
    
    return {"message": f"Marque '{name}' mise à jour avec succès vers '{marque.name}'"}

# Route pour supprimer une marque
@app.delete("/marques/{name}")
def delete_marque(name: str, db: Session = Depends(get_db)):
    db_marque = db.query(Marque).filter(Marque.name == name).first()  # Utilisation du modèle Marque
    if not db_marque:
        raise HTTPException(status_code=404, detail="Marque non trouvée")
    
    db.delete(db_marque)
    db.commit()
    
    return {"message": f"Marque '{name}' supprimée avec succès"}