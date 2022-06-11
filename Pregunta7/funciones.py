#Importamos librerias
import random

lista =[]
lsita2 =[]
fin = 20
def alea():

    for i in range (1, fin+1):
        lista.append(random.randint(0,100))
        lista2 = list(dict.fromkeys(lista))
    print(lista)
    return(lista2)
    
    

