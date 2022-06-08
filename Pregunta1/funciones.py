""" Realizara la división para poder calcular el % obtenido"""
# Importamos librerias
import errores as e
# Función
def dividir(x:int, y:int)->int :
    """Retorna la división de x / y"""
    if y == 0:
        return (e.get_err())
    else:
        return x / y




