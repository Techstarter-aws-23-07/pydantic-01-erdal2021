# Importiere benötigte Module
from pydantic import BaseModel

# Definition der main-Funktion
def main():
    # Ausgabe der gewünschten Nachricht
    print("AWS23/07")

# Definition der Person Klasse
class Person(BaseModel):
    firstname: str
    lastname: str
    email: str




# Prüfe, ob die main-Funktion direkt aufgerufen wird (nicht als Modul importiert)
if __name__ == "__main__":
    main()
