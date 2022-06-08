# Importamos librerias 
import funcion as f
# Constantes
MSG = """Bievenido: """
#Creamos lista
lista = []

def main():
    print(MSG)
    l = f.get_ing("Ingrese las calificaciones: ").split(",")
    try:
        lista = [int(x) for x in l]
        print (lista)
    except:
        print("Error de tipeo/Error de formato")
        return main()
# Mi programa
main()