def es_palindromo_recursivo(palabra):
    # 1. Caso Base: Si la palabra tiene 0 o 1 letra, es un palíndromo.
    if len(palabra) <= 1:
        # Mostramos que hemos llegado al caso base y es verdadero.
        print(f"Caso base: '{palabra}' es palíndromo.")
        return True
    
    # 2. Paso Recursivo: Comparamos los extremos.
    primera_letra = palabra[0]
    ultima_letra = palabra[-1]
    
    # Imprimimos la operación de comparación
    print(f"Comparando: '{primera_letra}' con '{ultima_letra}' en '{palabra}'")

    # Si las letras son iguales, continuamos con la subcadena (sin los extremos).
    if primera_letra == ultima_letra:
        # La subcadena va desde el índice 1 hasta el penúltimo (índice -1)
        subcadena = palabra[1:-1]
        
        # Llamada recursiva con la subcadena
        return es_palindromo_recursivo(subcadena)
    else:
        # Si las letras no son iguales, inmediatamente NO es palíndromo.
        print(f"'{primera_letra}' NO es igual a '{ultima_letra}'. NO es palíndromo.")
        return False

# Pruebas
print("\n--- Prueba 1: 'radar' ---")
print(f"Resultado final: {es_palindromo_recursivo('radar')}\n")

print("\n--- Prueba 2: 'python' ---")
print(f"Resultado final: {es_palindromo_recursivo('python')}")
