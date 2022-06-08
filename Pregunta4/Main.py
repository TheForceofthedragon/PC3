# Importamos librerias
import math
# Creamos la clase rectangulo
class rectangulo:
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
# Metodos
    def area(self):
        A = self.largo * self.ancho
        print("El área es:",A) 
# Creación de variable        
a = float(input("Ingrese el ancho: "))
l = float(input("Ingrese el largo: "))
# Creamos los objetos
circulo1 = rectangulo(a,l)
circulo1.area()