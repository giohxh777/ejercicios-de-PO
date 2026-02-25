class Cuchillo:

    def __init__(self, marca, filo):
        self.marca = marca
        self.filo = filo

    def hacer_corte(self, objeto):
        if self.filo <= 0:
            print("El cuchillo ha perdido su poder Necesita afilarse.")
            return objeto

        nueva_vida = objeto.get_vida() - 50
        objeto.set_vida(nueva_vida)

        self.filo -= 25
        print(f"Filo restante: {self.filo}%")

        if objeto.get_vida() <= 0:
            objeto.morir()

        return objeto

    def afilar(self):
        self.filo = 100
        print("El cuchillo ha sido afilado al 100%.")