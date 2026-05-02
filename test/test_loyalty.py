import pytest
from app.models import CarteFidelite, Facture, Fleur, Qualite
from datetime import date

def test_calcul_niveau_fidelite():
    fleur = Fleur(id=1, espece="Rose", date_coupe=date(2025,1,1), qualite=Qualite.SUPERIEURE, prix=100.99)
    # Prix facture avec TVA 20% = 121.188 -> 121.19
    facture = Facture(id=1, nom_client="Alice", date_vente=date(2025,1,2), fleurs=[fleur])
    
    carte = CarteFidelite(nom_client="Alice")
    carte.ajouter_facture(facture)
    
    assert carte.calculer_niveau() == "Bronze" # 121.19 < 200

def test_facture_date_invalide():
    fleur = Fleur(id=1, espece="Tulipe", date_coupe=date(2025,5,1), qualite=Qualite.STANDARD, prix=5.99)
    with pytest.raises(ValueError):
        # Vente avant la coupe
        Facture(id=2, nom_client="Bob", date_vente=date(2025,4,30), fleurs=[fleur])