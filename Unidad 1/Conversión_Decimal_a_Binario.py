def decimal_a_binario(numero_decimal):
    """
    Convierte un número decimal positivo a su representación binaria 
    utilizando una Pila.
    """
    if numero_decimal == 0:
        return "0"

    pila_residuos = []  # Usamos una lista de Python como Pila
    
    # Paso 1: Generar residuos y apilarlos (push)
    num_actual = numero_decimal
    while num_actual > 0:
        # Calcular el residuo (el bit binario)
        residuo = num_actual % 2
        
        # Apilar el residuo
        pila_residuos.append(residuo)
        
        # Actualizar el número (división entera)
        num_actual = num_actual // 2
    
    # Paso 2: Desapilar (pop) y concatenar para obtener el resultado LIFO
    cadena_binaria = ""
    while pila_residuos:
        # Desapilar el último residuo insertado (LIFO)
        bit = pila_residuos.pop()
        
        # Concatenar
        cadena_binaria += str(bit)
        
    return cadena_binaria

# --- Prueba con el ejemplo: 25 ---
numero_prueba = 25
resultado = decimal_a_binario(numero_prueba)

print(f"Número decimal: {numero_prueba}")
print(f"Número binario: {resultado}")
