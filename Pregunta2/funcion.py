
def get_ing(msg: str='recepciona los numeros ')->str:
    """Solicita un número entero"""
    try:
        x = str(input(msg))
        return x
    except:
        print("Error de tipeo/Error de formato")
        return get_ing(msg)
