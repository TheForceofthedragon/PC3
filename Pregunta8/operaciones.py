"""Contiene funcionalidades del tipo suma, resta, multiplicacion, división"""
import math

def sumar(x:float, y: float)->float :
    """Retorna la suma de x + y"""
    return x + y

def restar(x:float, y: float)->float :
    """Retorna la resta de x - y"""
    return x - y

def multiplicar(x:float, y: float)->float :
    """Retorna la multiplicacion de x * y"""
    return x * y

def dividir(x:float, y: float)->float :
    """Retorna la suma de x / y"""
    if x != 0 and y != 0: 
        return x / y
    elif x != 0 and y == 0:
        print("ERROR: No es posible dividir entre 0 ")
    else:
        try:
            x = float(input())
            return x
        except:
            return ("Vuelva a intentarlo ")