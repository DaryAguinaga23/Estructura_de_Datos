def esta_balanceada(expresion):
    """
    Verifica si una expresión tiene los paréntesis balanceados usando una pila.
    """
    pila = []  # Usamos una lista de Python como pila
    
    for simbolo in expresion:
        if simbolo == '(':
            # 1. Si es de apertura, lo apilamos (push)
            pila.append(simbolo)
        elif simbolo == ')':
            # 2. Si es de cierre, verificamos
            if not pila:
                # Caso A: La pila está vacía (cierre sin apertura)
                return False
            else:
                # Caso B: La pila no está vacía, desapilamos (pop) para emparejar
                pila.pop()
    
    # 3. Al terminar, si la pila está vacía, está balanceada
    return not pila

# --- Pruebas ---
expresion_1 = "((a+b)*(c/d))"
expresion_2 = "((x+y)*z"
expresion_3 = ")(a*b)"
expresion_4 = "a + b"

print(f"'{expresion_1}' está balanceada: {esta_balanceada(expresion_1)}") # Resultado: True
print(f"'{expresion_2}' está balanceada: {esta_balanceada(expresion_2)}") # Resultado: False (falta un cierre)
print(f"'{expresion_3}' está balanceada: {esta_balanceada(expresion_3)}") # Resultado: False (cierre inicial)
print(f"'{expresion_4}' está balanceada: {esta_balanceada(expresion_4)}") # Resultado: True (no hay paréntesis)
