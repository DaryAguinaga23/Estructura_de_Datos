class ConvertidorBase:
    """
    Convierte un número decimal a cualquier base (hasta base 16) utilizando una Pila.
    """
    def __init__(self):
        # Mapeo para residuos mayores a 9 (para bases como Hexadecimal)
        self.digitos = "0123456789ABCDEF"
        self.pila_residuos = [] 

    def convertir(self, numero_decimal, base):
        """
        Realiza la conversión del número decimal a la base especificada.
        """
        if not (2 <= base <= 16):
            return f"Error: La base {base} no está soportada (solo bases 2 a 16)."
        
        if numero_decimal == 0:
            return "0"

        self.pila_residuos.clear()
        num_actual = numero_decimal
        
        # Paso 1: Generar residuos y apilarlos (push)
        while num_actual > 0:
            # Calcular el residuo
            residuo = num_actual % base
            
            # Apilar el residuo
            self.pila_residuos.append(residuo)
            
            # Actualizar el número (división entera)
            num_actual = num_actual // base
        
        # Paso 2: Desapilar (pop) y concatenar (LIFO)
        resultado_final = ""
        while self.pila_residuos:
            # Desapilar y usar la tabla de mapeo (self.digitos)
            residuo = self.pila_residuos.pop()
            resultado_final += self.digitos[residuo]
            
        return resultado_final

# --- Simulación de uso ---
convertidor = ConvertidorBase()

# Ejemplo 1: Decimal 25 a Binario (Base 2) -> 11001
num1 = 25
base1 = 2
res1 = convertidor.convertir(num1, base1)
print(f"Decimal {num1} en Base {base1}: {res1}")

# Ejemplo 2: Decimal 42 a Octal (Base 8) -> 52
num2 = 42
base2 = 8
res2 = convertidor.convertir(num2, base2)
print(f"Decimal {num2} en Base {base2}: {res2}")

# Ejemplo 3: Decimal 255 a Hexadecimal (Base 16) -> FF
num3 = 255
base3 = 16
res3 = convertidor.convertir(num3, base3)
print(f"Decimal {num3} en Base {base3}: {res3}")
