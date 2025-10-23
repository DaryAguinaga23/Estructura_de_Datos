def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 2, 3, 4, 5]))  # 15

