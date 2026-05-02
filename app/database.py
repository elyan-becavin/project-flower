from typing import List
from app.models import Fleur, Qualite

class FlowerDatabase:
    def __init__(self):
        # Séparation physique logique des stocks
        self.flora_destock: List[Fleur] = []  # Qualité Standard/Dégradée
        self.flora_prestige: List[Fleur] = [] # Qualité Supérieure

    def ajouter_fleur(self, fleur: Fleur):
        if fleur.qualite == Qualite.SUPERIEURE:
            self.flora_prestige.append(fleur)
        else:
            self.flora_destock.append(fleur)

# Instance unique pour l'application
db = FlowerDatabase()