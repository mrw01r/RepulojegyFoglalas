class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, jarat):
        self.foglalasok.append(jarat)
        return f'Foglalás sikeres: {jarat.jaratszam} - {jarat.celallomas}\nÁr: {jarat.jegyar}'

    def lemondas(self, jarat):
        if jarat in self.foglalasok:
            self.foglalasok.remove(jarat)
            return f'{jarat.jaratszam} számú járat foglalása lemondva.'
        return 'A foglalás nem található.'

    def listar_foglalasok(self):
        return self.foglalasok