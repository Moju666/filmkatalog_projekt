#Hauptcode fuer Filmkatalog
#  # Dein Filmkatalog-Programm


filme = {} # Ein Dictionary zum Speichern der Filme. Schlüssel: Filmtitel, Wert: Dictionary mit Details

def filme_anzeigen():
    if not filme:
        print("Der Katalog ist leer.")
        return

    print("\n--- Dein Filmkatalog ---")
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

def film_hinzufuegen():
    print("\n--- Film hinzufügen ---")
    titel = input("Titel des Films: ")
    regisseur = input("Regisseur des Films: ")
    jahr = input("Erscheinungsjahr des Films: ")

    if titel in filme:
        print(f"Fehler: Film '{titel}' existiert bereits im Katalog.")
        return

    filme[titel] = {
        "regisseur": regisseur,
        "jahr": jahr
    }
    print(f"Film '{titel}' wurde hinzugefügt.")

# Test der Funktionen (werden später durch ein Menü ersetzt)
film_hinzufuegen()
filme_anzeigen()


def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Beenden")
    print("------------------------")

def main():
    while True: # Eine Endlosschleife für das Menü
        zeige_menue() # Zeige das Menü an
        wahl = input("Ihre Wahl: ") # Erfasse die Benutzereingabe

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            print("Programm wird beendet. Auf Wiedersehen!")
            break # Beende die Schleife und damit das Programm
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")



def film_suchen():
    print("\n--- Film suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff für den Titel ein: ").lower()
    gefundene_filme = {} # Dictionary, um die gefundenen Filme zu speichern

    # Iteriere durch alle Filme im Katalog
    for titel, details in filme.items():
        # Überprüfe, ob der Suchbegriff im Titel (kleingeschrieben) enthalten ist
        if suchbegriff in titel.lower():
            gefundene_filme[titel] = details # Füge den gefundenen Film hinzu

    # Wenn keine Filme gefunden wurden
    if not gefundene_filme:
        print(f"Keine Filme gefunden, die '{suchbegriff}' im Titel enthalten.")
        return

    print(f"\n--- Gefundene Filme für '{suchbegriff}' ---")
    # Zeige die Details der gefundenen Filme an (ähnlich wie filme_anzeigen)
    for titel, details in gefundene_filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")
def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Film suchen") # NEU
    print("4. Beenden")    # NUMMER GEÄNDERT
    print("------------------------")
def main():
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3': # NEU
            film_suchen()
        elif wahl == '4': # NUMMER GEÄNDERT
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
# Startet das Hauptprogramm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()
