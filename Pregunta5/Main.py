
# Creamos la clase alumno
class alumno:
    def __init__(self,nombre,registro):
        self.nombre = nombre
        self.registro = registro

# Metodos
    def display(self):
        print()
        print("El nombre del alumno es:",n)
        print("Su número de registro es:",r)
   
    def set_age(self):
        print("La edad del estudiante es:",edad)

    def set_nota(self):
        print("Las notas del estudiante son",lista)
        
# Creación de variable
lista = []        
n = input("Ingresa tu nombre: ")
r = int(input("Ingresa el número de registro: "))
edad = int(input("Ingrese la edad del estudiante: "))

while True:
    rpta = input("Desea ingresar notas: ")
    if rpta == "si":
        nota = float(input("Ingrese las notas del estudiante: "))
        lista.append(nota)
    elif rpta == "no":
        break

# Creamos los objetos
alum = alumno(n,r)
alum.display()
alum.set_age()
alum.set_nota()