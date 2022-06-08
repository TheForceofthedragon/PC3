# Importando librerias
import funciones as f
import errores as er
#Constantes
MSG = """Ingrese el nivel de gasolina en el formato x/y: """
# Funciones y/o clases
def main():
    print(MSG)
    variablex = er.get_int("Ingrese X: ")
    variabley = er.get_int("Ingrese Y: ")
    valor = f.dividir(variablex,variabley)
    while True:
        if valor <= 0.01:
            print("E")
        elif valor >= 0.25 and valor <0.5:
            print(f"Output: {int(valor*100)} %")
            break
        elif valor >= 0.4 and valor <0.75:
            print(f"Output: {int(valor*100)} %")
            break
        elif valor >= 0.75 and valor <1:
            print(f"Output: {int(valor*100)} %")
            break
        elif valor == 1:
            print("Output: F")
            break
        else:
            return main()
# Mi programa        
main()


