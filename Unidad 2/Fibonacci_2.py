def fibonacci(n):
    # Caso base: El valor es 0 o 1
    if n == 0 or n == 1:
        # Mostramos el valor base devuelto para ayudar a rastrear.
        # Esto ocurre muchas veces.
        # print(f"Caso base alcanzado: fibonacci({n}) devuelve {n}")
        return n
    else:
        # Llamadas recursivas para obtener los dos términos anteriores
        a = fibonacci(n - 1)
        b = fibonacci(n - 2)
        
        # Realizamos la suma
        resultado = a + b
        
        # Mostramos la operación de suma:
        print(f"Calculando fibonacci({n}): {a} + {b} = {resultado}")
        
        return resultado

print(f"\nCalculando fibonacci(6):\n")
print(f"El resultado final es: {fibonacci(6)}\n")
