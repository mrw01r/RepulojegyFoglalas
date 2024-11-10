class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, jarat):
        self.foglalasok.append(jarat)
        return f'Foglalás sikeres: {jarat.jaratszam} - {jarat.celallomas}\nÁr: {jarat.jegyar}'

    def lemondas(self, jaratszam):
        jaratszam = int(jaratszam)
        for jarat in self.foglalasok:
            if jarat.jaratszam == jaratszam:
                self.foglalasok.remove(jarat)
                return f'{jaratszam} számú járat foglalása lemondva.'
        return 'A foglalás nem található.'

    def listar_foglalasok(self):
        return self.foglalasok