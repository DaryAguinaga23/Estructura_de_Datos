def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        hanoi(1, origen, destino, auxiliar)
        hanoi(n-1, auxiliar, destino, origen)

hanoi(3, "A", "C", "B")
