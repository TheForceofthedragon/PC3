# Importamos librerias
import math
# Creamos la clase circulo 
class circulo:
    def __init__(self,radio):
        self.radio = radio
# Metodos
    def area(self):
        A = math.pi * self.radio * self.radio
        print("El área es:",A) 
# Creación de variable        
r = float(input("Ingrese el radio: "))
# Creamos los objetos
circulo1 = circulo(r)
circulo1.area()
