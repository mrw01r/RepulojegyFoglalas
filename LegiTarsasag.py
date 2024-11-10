class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def listar_jaratok(self):
        return self.jaratok