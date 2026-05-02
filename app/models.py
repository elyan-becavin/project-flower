from pydantic import BaseModel, field_validator, model_validator
from datetime import date
from typing import List, Optional
from enum import Enum

class Qualite(str, Enum):
    STANDARD = "standard"
    DEGRADEE = "degradee"
    SUPERIEURE = "superieure"

class Fleur(BaseModel):
    id: int
    espece: str
    date_coupe: date
    qualite: Qualite
    prix: float

    @field_validator('prix')
    @classmethod
    def check_prix_format(cls, v: float):
        if not str(v).endswith('.99'):
            raise ValueError("Le prix doit se terminer par .99")
        return v

class Facture(BaseModel):
    id: int
    nom_client: str
    date_vente: date
    fleurs: List[Fleur]
    prix_total: float = 0.0

    @model_validator(mode='after')
    def validate_facture(self):
        # Vérification des dates
        for fleur in self.fleurs:
            if self.date_vente < fleur.date_coupe:
                raise ValueError(f"La date de vente ne peut pas être antérieure à la coupe de la {fleur.espece}")
        
        # Calcul du prix avec TVA 20%
        somme_fleurs = sum(f.prix for f in self.fleurs)
        self.prix_total = round(somme_fleurs * 1.20, 2)
        return self

class CarteFidelite(BaseModel):
    nom_client: str
    factures: List[Facture] = []

    def ajouter_facture(self, facture: Facture):
        if facture.nom_client != self.nom_client:
            raise ValueError("La facture n'appartient pas au propriétaire de la carte")
        self.factures.append(facture)

    def reset_historique(self):
        self.factures = []

    def calculer_niveau(self) -> str:
        total = sum(f.prix_total for f in self.factures)
        if total < 200: return "Bronze"
        if total < 500: return "Argent"
        if total < 2000: return "Or"
        return "Platine" # Extension logique

    def factures_entre_dates(self, debut: date, fin: date) -> List[Facture]:
        return [f for f in self.factures if debut <= f.date_vente <= fin]