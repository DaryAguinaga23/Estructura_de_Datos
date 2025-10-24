def contar_caracter(cadena, caracter):
    if cadena == "":
        return 0
    else:
        if cadena[0] == caracter:
            return 1 + contar_caracter(cadena[1:], caracter)
        else:
            return contar_caracter(cadena[1:], caracter)

print(contar_caracter("banana", "a"))  # 3

