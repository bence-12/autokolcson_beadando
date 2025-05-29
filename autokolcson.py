class Auto:
    def __init__(self, rendszam, tipus, dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.dij = dij

class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

class Autokolcsonzo:
    def __init__(self):
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def berel(self, rendszam, datum):
        auto = self.keres_auto(rendszam)
        if not auto:
            return "Nincs ilyen rendszámú autó."
        if self.berelve_van(auto, datum):
            return "Ez az autó már ki van adva erre a napra."
        self.berlesek.append(Berles(auto, datum))
        return f"Bérlés sikeres. Ár: {auto.dij} Ft"

    def lemond(self, rendszam, datum):
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                self.berlesek.remove(b)
                return "Bérlés lemondva."
        return "Nem található ilyen bérlés."

    def listaz(self):
        if not self.berlesek:
            return "Nincs aktív bérlés."
        szoveg = ""
        for b in self.berlesek:
            szoveg += f"{b.auto.rendszam} - {b.auto.tipus} - {b.datum} - {b.auto.dij} Ft\n"
        return szoveg.strip()

    def keres_auto(self, rendszam):
        for a in self.autok:
            if a.rendszam == rendszam:
                return a
        return None

    def berelve_van(self, auto, datum):
        for b in self.berlesek:
            if b.auto == auto and b.datum == datum:
                return True
        return False

def fo():
    kolcsonzo = Autokolcsonzo()
    kolcsonzo.hozzaad_auto(Auto("ABC-123", "Toyota Corolla", 10000))
    kolcsonzo.hozzaad_auto(Auto("DEF-456", "Ford Transit", 15000))
    kolcsonzo.hozzaad_auto(Auto("GHI-789", "Opel Astra", 12000))

    kolcsonzo.berel("ABC-123", "2025-06-01")
    kolcsonzo.berel("DEF-456", "2025-06-02")
    kolcsonzo.berel("GHI-789", "2025-06-01")
    kolcsonzo.berel("ABC-123", "2025-06-03")

    while True:
        print("\n--- Autókölcsönző ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasz = input("Választás: ")

        if valasz == "1":
            r = input("Rendszám: ")
            d = input("Dátum (pl. 2025-06-01): ")
            print(kolcsonzo.berel(r, d))
        elif valasz == "2":
            r = input("Rendszám: ")
            d = input("Dátum: ")
            print(kolcsonzo.lemond(r, d))
        elif valasz == "3":
            print(kolcsonzo.listaz())
        elif valasz == "4":
            print("Viszlát!")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    fo()
