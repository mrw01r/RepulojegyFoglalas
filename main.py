from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from LegiTarsasag import LegiTarsasag
from  JegyFoglalas import JegyFoglalas

def main():
    legi_tarsasag = LegiTarsasag("Példa Airlines")

    jarat1 = BelfoldiJarat(1, "Budapest", 10000)
    jarat2 = NemzetkoziJarat(2, "London", 50000)
    jarat3 = NemzetkoziJarat(3, "New York", 100000)

    legi_tarsasag.hozzaad_jarat(jarat1)
    legi_tarsasag.hozzaad_jarat(jarat2)
    legi_tarsasag.hozzaad_jarat(jarat3)

    foglalas = JegyFoglalas()

    while True:
        print("\n1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            for i, jarat in enumerate(legi_tarsasag.listar_jaratok()):
                print(f"{i + 1}. Járatszám: {jarat.jaratszam}, Célállomás: {jarat.celallomas}, Ár: {jarat.jegyar}")

            jaratszam = int(input("Válaszd ki a foglalni kívánt járat számát: ")) - 1
            print(foglalas.foglalas(legi_tarsasag.jaratok[jaratszam]))

        elif valasztas == "2":
            for i, fogl in enumerate(foglalas.listar_foglalasok()):
                print(f"{i + 1}. Járatszám: {fogl.jaratszam}, Célállomás: {fogl.celallomas}, Ár: {fogl.jegyar}")

            jaratszam = int(input("Add meg a lemondani kívánt foglalás járatszámát: "))
            print(foglalas.lemondas(jaratszam))

        elif valasztas == "3":
            for fogl in foglalas.listar_foglalasok():
                print(f"Járatszám: {fogl.jaratszam}, Célállomás: {fogl.celallomas}, Ár: {fogl.jegyar}")

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás, próbáld újra.")


if __name__ == "__main__":
    main()