class TorresHanoi:
    """
    Clase para resolver el problema de las Torres de Hanoi mediante recursividad,
    una aplicación implícita de la estructura Pila (Stack).
    """
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.movimientos_totales = 0

    def resolver(self, origen="A", destino="C", auxiliar="B"):
        """
        Inicia el proceso de resolución y muestra el número total de movimientos.
        """
        print(f"--- Inicio de la solución para {self.num_discos} discos ---")
        print(f"Origen: {origen}, Destino: {destino}, Auxiliar: {auxiliar}\n")
        
        self.resolver_recursivo(self.num_discos, origen, destino, auxiliar)
        
        print(f"\n--- Proceso finalizado ---")
        print(f"Total de movimientos realizados: {self.movimientos_totales}")

    def resolver_recursivo(self, n, origen, destino, auxiliar):
        """
        Función recursiva que aplica la lógica de Hanoi.
        """
        if n == 1:
            # Caso Base: Mover el disco más pequeño
            print(f"Mover disco 1 de {origen} a {destino}")
            self.movimientos_totales += 1
            return

        # 1. Mover n-1 discos de Origen a Auxiliar, usando Destino como auxiliar.
        #    Esta es la primera llamada recursiva (PUSH en la Pila de llamadas).
        self.resolver_recursivo(n - 1, origen, auxiliar, destino)

        # 2. Mover el disco más grande restante (n) de Origen a Destino.
        print(f"Mover disco {n} de {origen} a {destino}")
        self.movimientos_totales += 1

        # 3. Mover n-1 discos de Auxiliar a Destino, usando Origen como auxiliar.
        #    Esta es la segunda llamada recursiva.
        self.resolver_recursivo(n - 1, auxiliar, destino, origen)


# --- Simulación de uso ---
num_discos = 3
juego = TorresHanoi(num_discos)
juego.resolver()
