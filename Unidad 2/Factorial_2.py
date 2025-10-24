def factorial(n):
    # Condición base: el factorial de 1 es 1
    if n == 1:
        # Se imprime el último valor, que es el de la condición base, pero no la operación
        # ya que la multiplicación comienza un nivel más arriba.
        return 1
    else:
        # **Se muestra la operación antes de la llamada recursiva**
        # Nota: La salida se ve al revés (del 2 * 1 al 5 * 4), porque las impresiones
        # se ejecutan en el orden en que se desenrolla la recursión (stack).
        resultado_parcial = n * factorial(n - 1)
        print(f"Calculando: {n} * factorial({n - 1}) = {resultado_parcial}")
        return resultado_parcial

print(f"\nEl resultado final es: {factorial(5)}\n")
