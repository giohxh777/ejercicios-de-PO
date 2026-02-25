class Ingredientes:

    def __init__(self, nombre, vida):
        self.nombre_vegetal = nombre
        self.vida_vegetal = vida

    def ver_info(self):
        return f"Nombre: {self.nombre_vegetal}, Vida: {self.vida_vegetal}"

    def get_vida(self):
        return self.vida_vegetal

    def set_vida(self, nueva_vida):
        self.vida_vegetal = nueva_vida

    def morir(self):
        print(f"{self.nombre_vegetal} ha sido completamente picado.")


class Tomate(Ingredientes):

    def __init__(self, nombre, vida, estado):
        super().__init__(nombre, vida)
        self.estado_vegetal = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado_vegetal = nuevo_estado

    def imprimir_info(self):
        return f"{self.ver_info()}, Estado: {self.estado_vegetal}"


class Cebolla(Ingredientes):
    pass


class Pasta:

    def __init__(self, nombre):
        self.nombre = nombre
        self.coccion = 0

    def hervir(self):
        self.coccion += 25
        if self.coccion > 100:
            self.coccion = 100

    def get_coccion(self):
        return self.coccion
       