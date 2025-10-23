def buscar_elemento(lista, elemento):
    if not lista:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return buscar_elemento(lista[1:], elemento)

print(buscar_elemento([1, 3, 5, 7], 5))  # True
