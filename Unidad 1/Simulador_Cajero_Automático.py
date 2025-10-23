from collections import deque

class Cliente:
    """Representa a un cliente con su nombre y el tipo de transacción."""
    def __init__(self, nombre, transaccion):
        self.nombre = nombre
        self.transaccion = transaccion

    def __str__(self):
        return f"Cliente({self.nombre}, {self.transaccion})"

class ColaCajero:
    """Simula el flujo de clientes en un cajero usando una cola FIFO."""
    def __init__(self):
        # Usamos deque para una implementación eficiente de cola
        self.cola = deque()

    def llega_cliente(self, cliente):
        """Agrega un cliente al final de la cola (Enqueue)."""
        self.cola.append(cliente)
        print(f"[LLEGADA] {cliente.nombre} se ha unido a la fila para: {cliente.transaccion}")

    def atender_siguiente(self):
        """
        Elimina y devuelve el cliente del frente de la cola (Dequeue)
        para ser atendido.
        """
        if not self.esta_vacia():
            cliente_atendido = self.cola.popleft() # FIFO: El primero en entrar, sale primero
            print(f"[ATENCION] Cajero atiende a {cliente_atendido.nombre} para su {cliente_atendido.transaccion}.")
            return cliente_atendido
        else:
            print("[INFO] No hay clientes en la fila.")
            return None

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.cola) == 0

    def mostrar_estado(self):
        """Muestra el estado actual de la cola."""
        if self.esta_vacia():
            print(">>> La cola está vacía.")
        else:
            nombres_en_fila = [cliente.nombre for cliente in self.cola]
            print(f">>> Fila actual ({len(self.cola)} clientes): {nombres_en_fila}")
        print("-" * 35)

# --- Simulación de uso ---
cajero = ColaCajero()

# Llegada de clientes
print("--- COMIENZO DE LA SIMULACIÓN ---")
cajero.mostrar_estado()

cliente_A = Cliente("Alicia", "Retiro")
cliente_B = Cliente("Bernardo", "Depósito")
cliente_C = Cliente("Camila", "Consulta")

cajero.llega_cliente(cliente_A) # Llega primero
cajero.llega_cliente(cliente_B) # Llega segundo
cajero.llega_cliente(cliente_C) # Llega tercero

cajero.mostrar_estado()

# Atención de clientes (FIFO)
print("\n--- PROCESO DE ATENCIÓN (FIFO) ---")
cajero.atender_siguiente()  # Atiende a Alicia (primera en llegar)
cajero.mostrar_estado()

cajero.atender_siguiente()  # Atiende a Bernardo
cajero.mostrar_estado()

cajero.atender_siguiente()  # Atiende a Camila
cajero.mostrar_estado()

# Intentar atender sin clientes
cajero.atender_siguiente()
