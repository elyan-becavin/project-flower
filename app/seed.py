from app.database import db
from app.models import Fleur, Qualite
from datetime import date

def populate_db():
    donnees = [
        Fleur(id=1, espece="Rose", date_coupe=date(2025, 4, 20), qualite=Qualite.SUPERIEURE, prix=19.99),
        Fleur(id=2, espece="Tulipe", date_coupe=date(2025, 4, 25), qualite=Qualite.STANDARD, prix=4.99),
        Fleur(id=3, espece="Œillet", date_coupe=date(2025, 4, 26), qualite=Qualite.DEGRADEE, prix=2.99),
        Fleur(id=4, espece="Lys", date_coupe=date(2025, 4, 22), qualite=Qualite.SUPERIEURE, prix=25.99),
    ]
    for f in donnees:
        db.ajouter_fleur(f)
    print("Bases de données initialisées avec succès.")

if __name__ == "__main__":
    populate_db()