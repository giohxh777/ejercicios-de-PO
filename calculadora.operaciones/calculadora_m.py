class Calculadora:
    def __init__(self, usuario, num1, num2, fecha): 
        self.usuario = usuario
        self.numero1 = num1
        self.numero2 = num2
        self.fecha = fecha
        
    def get_usuario(self):
            return self.usuario
        
    def set_usuario(self, nuevo_usuario):
            self.usuario = nuevo_usuario
    
    def get_numero1(self):
            return self.numero1
        
    def set_numero1(self, nuevo_numero1):
            self.numero1 = nuevo_numero1
            
    def get_numero2(self):
            return self.numero2
        
    def set_numero2(self, nuevo_numero2):
            self.numero2 = nuevo_numero2

    def get_fecha(self):
            return self.fecha   
    
    def set_fecha(self, nueva_fecha):
            self.fecha = nueva_fecha
            
    def calcular_sumar(self, num1, num2):
        resultado_suma = num1 + num2
        print("El resultado de la suma es: ", [resultado_suma])
        return resultado_suma
    
    def calcular_restar(self, num1, num2):
        resultado_resta = num1 - num2
        print("El resultado de la resta es: ", [resultado_resta])
        return resultado_resta
    
    def calcular_multiplicar(self, num1, num2):
        resultado_multiplicacion = num1 * num2
        print("El resultado de la multiplicación es: ", [resultado_multiplicacion])
        return resultado_multiplicacion
    
    def calcular_dividir(self, num1, num2):
        if num2 == 0:
            print("No se puede dividir por cero")
            return 
        else:
                resultado_division = num1 / num2
                print("El resultado de la división es: ", [resultado_division])
                return resultado_division        
        
        
    def tomar_fecha(self, fecha):
        self.fecha = fecha
        return self.fecha
        
        def mostrar_fecha(self):
            print(f"Fecha: {self.fecha}")
 
 
 


        
         
          
      