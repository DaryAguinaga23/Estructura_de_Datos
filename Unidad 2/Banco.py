class Cliente:
    def __init__(self, nombre, tiempo_llegada):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada

    def __str__(self):
        return f"({self.nombre}, Llegada: {self.tiempo_llegada} min)"

class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, dato):
        self.items.append(dato)
    
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0

def simular_atencion_recursiva(cola):
    if cola.is_empty():
        print("Fin de la simulación. La cola de atención está vacía.")
        return

    cliente_atendido = cola.dequeue()
    print(f"  Atendiendo a: {cliente_atendido.nombre} (Llegó en el minuto {cliente_atendido.tiempo_llegada})")

    simular_atencion_recursiva(cola)

cola_banco = Cola()

cola_banco.enqueue(Cliente("Ana", 0))
cola_banco.enqueue(Cliente("Luis", 3))
cola_banco.enqueue(Cliente("Maria", 5))
cola_banco.enqueue(Cliente("Pedro", 8))

print("--- Simulación de Atención en Banco (Recursiva) ---")
print("Clientes en cola (orden de llegada):")

for cliente in cola_banco.items:
    print(f"  -> {cliente}")

print("\nInicio de atención:")

simular_atencion_recursiva(cola_banco)
