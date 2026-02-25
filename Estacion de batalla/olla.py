class Olla:

    def __init__(self):
        self.contenido = []

    def agregar(self, ingrediente):
        self.contenido.append(ingrediente)
        print(f"{ingrediente.nombre_vegetal} agregado a la olla.")

    def mostrar_contenido(self):
        print("Contenido de la olla:")
        for item in self.contenido:
            print("-", item.nombre_vegetal)