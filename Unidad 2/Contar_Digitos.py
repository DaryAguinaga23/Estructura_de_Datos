def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1
