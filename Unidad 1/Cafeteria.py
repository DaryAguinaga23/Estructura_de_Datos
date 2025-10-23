class OrdenCafeteria:
    """Representa una orden de cliente."""
    def __init__(self, cliente, articulo):
        self.cliente = cliente
        self.articulo = articulo

    def __str__(self):
        return f"Orden de {self.cliente}: {self.articulo}"

class GestorOrdenes:
    """
    Gestiona las órdenes de la cafetería usando una Cola FIFO implementada
    con una lista estándar de Python.
    """
    def __init__(self):
        # Implementación de la Cola (Queue) con una lista estándar de Python
        self.cola = [] 

    def tomar_orden(self, cliente, articulo):
        """Agrega una nueva orden al final de la cola (Enqueue)."""
        nueva_orden = OrdenCafeteria(cliente, articulo)
        self.cola.append(nueva_orden) # Enqueue (al final)
        print(f"[RECIBIDA] {nueva_orden}")

    def preparar_siguiente_orden(self):
        """
        Extrae y prepara la orden del frente de la cola (Dequeue).
        """
        if not self.cola:
            print("[INFO] No hay órdenes pendientes en la cocina.")
            return None

        # Dequeue (al frente - índice 0). El uso de pop(0) asegura FIFO.
        orden_a_preparar = self.cola.pop(0) 
        
        print(f"\n[PREPARANDO] --> {orden_a_preparar.articulo} para {orden_a_preparar.cliente}...")
        print(f"[ENTREGADA] Orden completada: {orden_a_preparar.articulo}")
        
        return orden_a_preparar

    def mostrar_estado(self):
        """Muestra el número y el frente de la cola."""
        print("-" * 50)
        print(f"Órdenes pendientes en cocina: {len(self.cola)}")
        if self.cola:
            siguiente_orden = self.cola[0]
            print(f"Próxima a preparar (Frente): {siguiente_orden.articulo} para {siguiente_orden.cliente}")
        else:
            print("La cola de órdenes está vacía.")
        print("-" * 50)

# --- Simulación de uso ---
gestor = GestorOrdenes()

# 1. Llegan las órdenes
gestor.tomar_orden("Ana", "Café Americano")        # Llega primero
gestor.tomar_orden("Carlos", "Sándwich de Huevo")  # Llega segundo
gestor.tomar_orden("David", "Latte Vainilla")     # Llega tercero

gestor.mostrar_estado()

# 2. La cocina empieza a preparar (FIFO)
print("\n--- COMIENZO DE PREPARACIÓN (FIFO) ---")
gestor.preparar_siguiente_orden() # Debe ser Ana (Primera en llegar)

gestor.mostrar_estado()

gestor.preparar_siguiente_orden() # Debe ser Carlos

gestor.preparar_siguiente_orden() # Debe ser David

gestor.mostrar_estado()

gestor.preparar_siguiente_orden() # Intentar preparar sin órdenes
