import sys
from Test import add, divide

def main():
    print("=== Starte Mathematische Anwendung (Build Check) ===")
    
    # Ein paar Beispielberechnungen durchführen
    ergebnis_add = add(10, 20)
    ergebnis_div = divide(100, 4)
    
    print(f"Berechnung erfolgreich! 10 + 20 = {ergebnis_add}")
    print(f"Berechnung erfolgreich! 100 / 4 = {ergebnis_div}")
    print("=== Anwendung erfolgreich ausgeführt ===")

if __name__ == "__main__":
    # Falls dieses Skript direkt aufgerufen wird, starte die main-Funktion
    main()