from collections import deque

class JuegoDeTurnos:
    """
    Simula un ciclo de turnos de jugadores usando una Cola Circular.
    """
    def __init__(self, jugadores):
        # Inicializa la cola con la lista de jugadores
        self.cola_turnos = deque(jugadores)
        print(f"Juego iniciado. Orden inicial: {list(self.cola_turnos)}")
        print("-" * 40)

    def tomar_turno(self):
        """
        El jugador del frente toma su turno.
        Luego, se mueve al final de la cola para el siguiente ciclo.
        """
        if not self.cola_turnos:
            print("[INFO] No hay jugadores en el juego.")
            return

        # 1. Sacar al jugador del frente (Dequeue)
        jugador_actual = self.cola_turnos.popleft()
        
        print(f"--> TURNO: {jugador_actual}")
        
        # 2. Reinsertar al jugador al final (Enqueue) para el siguiente turno (Comportamiento Circular)
        self.cola_turnos.append(jugador_actual)
        
        print(f"    Siguiente turno: {self.cola_turnos[0]}")
        print(f"    Cola de espera: {list(self.cola_turnos)[1:]}")
        print("-" * 40)
        
        return jugador_actual

    def eliminar_jugador(self, jugador):
        """Permite que un jugador sea removido permanentemente del ciclo."""
        try:
            # Remover de la cola. Nota: Buscar y remover en deque es O(n).
            self.cola_turnos.remove(jugador)
            print(f"[REMOVIDO] {jugador} ha sido eliminado del ciclo.")
            print(f"    Nueva cola: {list(self.cola_turnos)}")
        except ValueError:
            print(f"[ERROR] {jugador} no se encuentra en la cola.")
        print("-" * 40)


# --- Simulación de uso ---
jugadores_iniciales = ["Alice", "Bob", "Charlie", "David"]
juego = JuegoDeTurnos(jugadores_iniciales)

# Ronda 1 (Ciclo completo)
juego.tomar_turno() # Alice
juego.tomar_turno() # Bob
juego.tomar_turno() # Charlie
juego.tomar_turno() # David (Alice debe ser el siguiente)

# Un jugador es eliminado
juego.eliminar_jugador("Bob")

# Ronda 2 (Alice sigue siendo la primera, pero Bob ya no está)
juego.tomar_turno() # Alice
juego.tomar_turno() # Charlie
