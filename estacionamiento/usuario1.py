
class Usuario: 
    def __init__(self, nombre, cedula, tipo_usuario):
        self.nombre = nombre 
        self.cedula = cedula
        self.tipo_usuario = tipo_usuario
        
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre 
        
    def get_cedula(self):
        return self.cedula
    def set_cedula(self, nueva_cedula):
        self.cedula = nueva_cedula
        
    def get_tipo_usuario(self):
        return self.tipo_usuario
    def set_tipo_usuario (self, nuevo_tipo_usuario):
        self.tipo_usuario = nuevo_tipo_usuario
    
    def imprimir_dato(self):
        print(f"nombre: {self.nombre}")
        print(f"cedula: {self.cedula}")
        print(f"tipo_ususario: {self.tipo_usuario}")
        
    