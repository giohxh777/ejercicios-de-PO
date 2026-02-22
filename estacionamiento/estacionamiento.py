from usuario1 import Usuario
from carro1 import Carro

class Estacionamiento:
    def __init__(self):
        self.puesto = ""
        self.fecha_entrada = ""
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = "libre"
        self.cliente = ""
        self.carro = ""
        self.atributos = ""
        
    def set_puesto(self, nuevo_puesto):
        self.puesto = nuevo_puesto    
    
    def registrar_entrada(self, cliente, carro):
        if self.estado == "libre":
            self.cliente = cliente
            self.carro = carro
            self.fecha_entrada = "22-02-2026"
            self.hora_entrada = "1:40"
            self.estado = "ocupado"
            print("Entrada registrada correctamente.")
        else:
            print("El puesto ya está ocupado.")

    def registrar_salida(self, placa_buscar):
        if self.estado == "ocupado":
            
            if self.carro.get_placa() == placa_buscar:
                self.hora_salida = "3:00"
                self.estado = "libre"
                print("Salida registrada correctamente.")
                print("Hora de salida:", self.hora_salida)
                
                self.guardar()
            else:
                print("La placa ingresada no coincide.")
        else:
            print("El puesto ya está libre.")

    def guardar(self):
        self.atributos += (
            f"{self.puesto:^10}"
            f"{self.estado:^10}"
            f"{self.fecha_entrada:^15}"
            f"{self.hora_entrada:^15}"
            f"{self.hora_salida:^15}\n"
            )
        

    def mostrar_info(self):
     print()
     print("TABLA DE REGISTRO".center(65))
     print("-" * 65)
     print(f"{'|Puesto':^10}|{'Estado':^10}|{'Fecha Entrada':^15}|{'Hora Entrada':^15}|{'Hora Salida|':^15}")
     print("-" * 65)
     print(self.atributos)