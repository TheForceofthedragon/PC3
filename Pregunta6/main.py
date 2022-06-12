# Importamos librerias
import math
from re import X
from tkinter import Y
# Creamos la clase circulo 
class punto:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
# Metodos
    def __str__(self):
        return "({}, {})".format(X,Y)
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} Pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )
    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(
            self, p, d))
class Rectangulo:
    def __init__(self, pInicial = punto(), pFinal = punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )
    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )
    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )
       

# Creación de variable        
A = punto(2,3)
B = punto(5,5)
C = punto(-3, -1)
D = punto(0,0)
# Creamos los objetos
circulo1 = punto()
circulo1.cuadrante()
circulo1.distancia(D)
circulo1.distancia(D)
circulo1.vector(B)
circulo1.vector(A)
R = Rectangulo(A,B)
R.altura()
R.base()
R.area()
