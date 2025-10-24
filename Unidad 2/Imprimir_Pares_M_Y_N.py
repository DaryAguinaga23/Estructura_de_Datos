def imprimirImparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo.")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero mayor que m.")

    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n
    imprimirImparesEntreMyNAux(m, n)

def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        print()
    else:
        print(m, end = " ")
        imprimirImparesEntreMyNAux(m + 2, n)
