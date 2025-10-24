def combinaciones(cadena, actual=""):
    if cadena == "":
        print(actual)
    else:
        combinaciones(cadena[1:], actual + cadena[0])
        combinaciones(cadena[1:], actual)

combinaciones("ab")
