from collections import deque

class ProcesadorASCII:
    """
    Clase para procesar una cadena de texto y distribuir sus caracteres 
    entre una Pila y una Cola basándose en el valor de su código ASCII.
    
    Criterio:
    - Código ASCII Par: Se inserta en la Pila (LIFO).
    - Código ASCII Impar: Se inserta en la Cola (FIFO).
    """
    
    def __init__(self):
        # La Pila se implementa con una lista (LIFO)
        self.pila_ascii_par = []
        # La Cola se implementa con deque (FIFO)
        self.cola_ascii_impar = deque()

    def procesar_cadena(self, texto):
        """
        Itera sobre la cadena, obtiene el código ASCII de cada carácter y lo 
        distribuye en la Pila o la Cola.
        """
        # Limpiar estructuras antes de empezar
        self.pila_ascii_par.clear()
        self.cola_ascii_impar.clear()
        
        print(f"--- Procesando cadena: '{texto}' ---")
        
        for caracter in texto:
            # Obtener el valor numérico ASCII
            codigo_ascii = ord(caracter)
            
            # Clasificación y distribución
            if codigo_ascii % 2 == 0:
                # Código Par -> Pila (PUSH)
                self.pila_ascii_par.append(caracter)
                print(f"'{caracter}' (ASCII {codigo_ascii}) -> Pila (Par)")
            else:
                # Código Impar -> Cola (ENQUEUE)
                self.cola_ascii_impar.append(caracter)
                print(f"'{caracter}' (ASCII {codigo_ascii}) -> Cola (Impar)")
        
        print("\n--- Resultado de la Distribución ---")

    def mostrar_estructuras(self):
        """Muestra el contenido actual de la Pila y la Cola."""
        
        # Mostrar Pila (último en entrar es el último elemento de la lista)
        print(f"Pila de Código Par (LIFO): {self.pila_ascii_par}")
        
        # Mostrar Cola (el primer elemento es el del frente)
        print(f"Cola de Código Impar (FIFO): {list(self.cola_ascii_impar)}")
        print("-" * 50)

# --- Simulación de uso ---
procesador = ProcesadorASCII()

cadena_prueba = "A5B4C3" # Mezcla de letras y números para variedad de ASCII
# Códigos ASCII: A=65(Impar), 5=53(Impar), B=66(Par), 4=52(Par), C=67(Impar), 3=51(Impar)

procesador.procesar_cadena(cadena_prueba)
procesador.mostrar_estructuras()
