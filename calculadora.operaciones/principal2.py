from usuario import Usuario
from numero import Numero
from calculadora_m import Calculadora                          
    
usuario1 = Usuario("GIO", "1093591113")
Numero= numero1 = (6)
Numero = numero2 =(9)

mostear_info_usuario = usuario1.mostrar_info()

calculadora1 = Calculadora(usuario1, numero1, numero2, "03-06-2006")


suma = calculadora1.calcular_sumar(numero1, numero2)
resta = calculadora1.calcular_restar(numero1, numero2)
multiplicacion = calculadora1.calcular_multiplicar(numero1, numero2)
division = calculadora1.calcular_dividir(numero1, numero2)

fecha1 = calculadora1.get_fecha()
fecha = calculadora1.set_fecha("03-06-2006")

mostrar_fecha_calculadora = input(str(calculadora1.fecha))