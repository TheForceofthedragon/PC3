def get_int(msg: str='Tipo de dato no valido: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        print("ERROR: Tipo de dato no valido ")
        return get_int(msg)

def get_float(msg: str='Ingrese un número decimal: ')->float:
    """Solicita un número decimal"""
    try:
        x = float(input(msg))
        return x
    except:
        return get_float(msg)