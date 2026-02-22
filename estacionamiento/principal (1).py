from usuario1 import Usuario
from carro1 import Carro
from estacionamiento import Estacionamiento

nombre = input("Ingrese nombre del cliente: ")
cedula = int(input("Ingrese cedula del cliente: "))
tipo_usuario = input("Ingrese tipo de usuario: ")
cliente = (nombre, cedula)

placa = input("Ingrese placa del carro: ")
marca = input("Ingrese la marca del carro: ")
color = input("Ingrese color del carro: ")

obj_carro = Carro(marca, color, placa)
obj_estacionamiento = Estacionamiento()

puesto = int(input("Ingrese el numero de puesto: "))
obj_estacionamiento.set_puesto(puesto)

obj_estacionamiento.registrar_entrada(cliente, obj_carro)
obj_estacionamiento.guardar()
obj_estacionamiento.mostrar_info()

registrar_salida = input("¿Desea ingresar la salida de un carro? si/no ")

if registrar_salida.lower() == "si":
    placa = input("Ingrese la placa del carro para dar salida: ")
    obj_estacionamiento.registrar_salida(placa)

elif registrar_salida.lower() == "no":
    print("No se registrará la salida de ningún carro.")

obj_estacionamiento.mostrar_info()