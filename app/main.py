from fastapi import FastAPI, HTTPException
from app.models import Fleur, Qualite
from typing import List
import uvicorn

app = FastAPI(title="Flora API")

# Simulation de deux bases de données (In-memory pour l'exemple, ou via fichiers)
db_destock = []  # FloraDestock (Standard/Dégradée)
db_prestige = [] # FloraPrestige (Supérieure)

@app.get("/fleurs", response_model=List[Fleur])
def get_fleurs(min_prix: float = 0, max_prix: float = 1000):
    all_fleurs = db_destock + db_prestige
    return [f for f in all_fleurs if min_prix <= f.prix <= max_prix]

@app.post("/fleurs/{magasin}")
def add_fleur(magasin: str, fleur: Fleur):
    if magasin == "destock":
        if fleur.qualite == Qualite.SUPERIEURE:
            raise HTTPException(status_code=400, detail="Qualité non acceptée ici")
        db_destock.append(fleur)
    elif magasin == "prestige":
        if fleur.qualite != Qualite.SUPERIEURE:
            raise HTTPException(status_code=400, detail="Seule la qualité supérieure est acceptée")
        db_prestige.append(fleur)
    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=89236)