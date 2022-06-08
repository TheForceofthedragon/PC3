# Funciones
def get_int(msg: str='Ingrese un número entero: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except:
        return get_int(msg)

def get_float(msg: str='Ingrese un número decimal: ')->float:
    """Solicita un número decimal"""
    try:
        x = float(input(msg))
        return x
    except:
        return get_float(msg)

def get_err(msg: str='Ingrese un valor diferente de 0: ')->int:
    """Solicita un número decimal"""
    try:
        y = int(input(msg))
        return y
    except:
        return get_err(msg)