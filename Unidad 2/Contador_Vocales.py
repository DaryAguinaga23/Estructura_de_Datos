def contar_vocales(cadena):
    if cadena == "":
        return 0
    else:
        if cadena[0].lower() in 'aeiou':
            return 1 + contar_vocales(cadena[1:])
        else:
            return contar_vocales(cadena[1:])

print(contar_vocales("Recursividad"))  # 5
