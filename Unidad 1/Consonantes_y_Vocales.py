class AnalizadorTexto:
    """
    Clase para analizar una cadena y clasificar sus caracteres alfabéticos 
    en vocales y consonantes.
    
    Esta operación podría usarse antes de insertar caracteres en una 
    estructura de datos basada en su tipo.
    """
    
    def __init__(self):
        # Definición de vocales (tanto mayúsculas como minúsculas)
        self.VOCALES = "aeiouAEIOUáéíóúÁÉÍÓÚ"

    def analizar_cadena(self, texto):
        """
        Clasifica los caracteres alfabéticos de la cadena en vocales y consonantes.
        
        Args:
            texto (str): La cadena de texto a analizar.
            
        Returns:
            dict: Un diccionario con las listas de 'vocales' y 'consonantes'.
        """
        
        vocales_encontradas = []
        consonantes_encontradas = []
        
        for caracter in texto:
            # 1. Ignorar caracteres que no son letras (espacios, números, símbolos)
            if not caracter.isalpha():
                continue
            
            # 2. Clasificar el carácter alfabético
            if caracter in self.VOCALES:
                vocales_encontradas.append(caracter)
            else:
                consonantes_encontradas.append(caracter)
                
        return {
            "vocales": vocales_encontradas,
            "consonantes": consonantes_encontradas
        }

    def procesar_con_pila_o_cola(self, texto):
        """
        Ejemplo conceptual: cómo se usarían los resultados para una Pila o Cola.
        En este ejemplo, encolamos las vocales y apilamos las consonantes.
        """
        from collections import deque
        
        resultados = self.analizar_cadena(texto)
        
        # Estructuras de datos a utilizar
        pila_consonantes = [] # Pila para consonantes (LIFO)
        cola_vocales = deque() # Cola para vocales (FIFO)
        
        # Apilar las consonantes
        for cons in resultados['consonantes']:
            pila_consonantes.append(cons)
            
        # Encolar las vocales
        for vocal in resultados['vocales']:
            cola_vocales.append(vocal)
            
        print("\n[EJEMPLO DE ESTRUCTURAS DE DATOS]")
        print(f"Texto original: '{texto}'")
        print(f"Pila de Consonantes (LIFO): {pila_consonantes}")
        print(f"Cola de Vocales (FIFO): {list(cola_vocales)}")
        print("-" * 50)


# --- Simulación de uso ---
analizador = AnalizadorTexto()
cadena_prueba = "Programacion en Python, 2024!"

resultados_analisis = analizador.analizar_cadena(cadena_prueba)

print(f"--- Análisis de Vocales y Consonantes ---")
print(f"Cadena: '{cadena_prueba}'")
print("-" * 50)

print(f"Vocales encontradas ({len(resultados_analisis['vocales'])}): {resultados_analisis['vocales']}")
print(f"Consonantes encontradas ({len(resultados_analisis['consonantes'])}): {resultados_analisis['consonantes']}")

# Demostración del uso de los datos en estructuras de datos
analizador.procesar_con_pila_o_cola(cadena_prueba)
