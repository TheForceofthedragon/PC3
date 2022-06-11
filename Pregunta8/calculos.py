# Importamos librerias
import operaciones as op
import Ingreso_datos as id
# Constantes
MSG = "Bienvenido"
MSG2 = """¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Multiplicar dos números
    3) Dividir dos números
    4) Restar dos números
    5) Salir 
    Ingrese opción: """
# Funciones y/o clases
def main():
    print(MSG)
    while True:
        opcion = int(input(MSG2))
        if opcion == 1:
            n1 = id.get_int("Ingrese el primer número: ")
            n2 = id.get_int("Ingrese el segundo número: ")
            s = op.sumar(n1,n2)
            print(f"la suma de los números es  : {s}")
        elif opcion == 2:
            n1 = id.get_int("Ingrese el primer número: ")
            n2 = id.get_int("Ingrese el segundo número: ")
            m = op.multiplicar(n1,n2)
            print(f"la multiplicación de los números es  : {m}")
        elif opcion == 3:
            n1 = id.get_int("Ingrese el primer número: ")
            n2 = id.get_int("Ingrese el segundo número: ")
            d = op.dividir(n1,n2)
            print(f"la división de los números es  : {d}")
        elif opcion == 4:
            n1 = id.get_int("Ingrese el primer número: ")
            n2 = id.get_int("Ingrese el segundo número: ")
            r = op.restar(n1,n2)
            print(f"la resta de los números es  : {r}")
        elif opcion == 5:
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
  
# Mi programa
main()