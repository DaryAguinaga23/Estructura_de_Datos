def permutaciones(lista, inicio=0):
    if inicio == len(lista) - 1:
        print(lista)
    else:
        for i in range(inicio, len(lista)):
            lista[inicio], lista[i] = lista[i], lista[inicio]
            permutaciones(lista, inicio + 1)
            lista[inicio], lista[i] = lista[i], lista[inicio]

permutaciones([1, 2, 3])
