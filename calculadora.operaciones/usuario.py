class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def set_nombre_usuario (self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def get_nombre_usuario(self):
        return self.nombre
    
    def set_cedula_usuario (self, nueva_cedula):
        self.cedula = nueva_cedula
        
    def get_cedula_usuario(self):
        return self.cedula
    
    def mostrar_info(self):
        print(f"Nombre del usuario: {self.nombre}")
        print(f"Cédula del usuario: {self.cedula}")