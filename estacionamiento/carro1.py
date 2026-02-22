class Carro :
   def __init__(self, marca_carro, color, placa):
       self.marca_carro = marca_carro
       self.color = color
       self.placa = placa 
       
   def get_marca_carro(self):
       return self.marca_carro
   def set_marca_carro(self, nueva_marca_carro):
       self.marca_carro = nueva_marca_carro
       
   def get_color(self):
       return self.color
   def set_color(self, nuevo_color):
       self.color = nuevo_color
       
   def get_placa(self):
       return self.placa
   def set_placa(self, nueva_placa):
       self.placa = nueva_placa
   
   def imprimir_datos(self):
       print (f"marca_carro:  {self.marca_carro}") 
       print (f"color:  {self.color}")  
       print (f"placa:  {self.placa}")   
        