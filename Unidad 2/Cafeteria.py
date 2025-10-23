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
        self.cola.append(nueva_orden) 
        print(f"[RECIBIDA] {nueva_orden}")

    def preparar_siguiente_orden(self):
        """
        Extrae y prepara la orden del frente de la cola (Dequeue).
        """
        if not self.cola:
            return None

        # Dequeue (al frente - índice 0).
        orden_a_preparar = self.cola.pop(0) 
        
        print(f"\n[PREPARANDO] --> {orden_a_preparar.articulo} para {orden_a_preparar.cliente}...")
        print(f"[ENTREGADA] Orden completada: {orden_a_preparar.articulo}")
        
        return orden_a_preparar

    def procesar_cola_recursivamente(self):
        """
        Procesa la cola de órdenes llamando recursivamente al proceso
        de preparación (simulando que se atiende una orden tras otra).
        """
        # Caso Base: Si la cola está vacía, terminamos.
        if not self.cola:
            print("[INFO] La cola de órdenes ha sido procesada completamente.")
            return

        # Paso Recursivo:
        # 1. Prepara y entrega la orden del frente.
        self.preparar_siguiente_orden()
        
        # 2. Llama a la función de nuevo para procesar la siguiente orden.
        self.procesar_cola_recursivamente()


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


gestor = GestorOrdenes()

# 1. Llegan las órdenes
gestor.tomar_orden("Ana", "Café Americano")
gestor.tomar_orden("Carlos", "Sándwich de Huevo")
gestor.tomar_orden("David", "Latte Vainilla")

gestor.mostrar_estado()

# 2. La cocina procesa TODAS las órdenes de forma recursiva (FIFO)
print("\n--- COMIENZO DE PROCESAMIENTO RECURSIVO (FIFO) ---")
gestor.procesar_cola_recursivamente() 

# 3. Mostrar el estado final
gestor.mostrar_estado()

# 4. Intentar procesar una cola ya vacía
print("\n--- Intentando procesar cola vacía ---")
gestor.procesar_cola_recursivamente()
