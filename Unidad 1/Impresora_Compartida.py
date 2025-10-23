from collections import deque
import time

class Documento:
    """Representa un documento en la cola de impresión."""
    def __init__(self, nombre, tamano_paginas):
        self.nombre = nombre
        self.tamano = tamano_paginas

    def __str__(self):
        return f"Documento('{self.nombre}', {self.tamano} páginas)"

class ColaImpresion:
    """Simula una cola de impresión FIFO."""
    def __init__(self):
        self.cola = deque()

    def enviar_documento(self, documento):
        """Agrega un documento al final de la cola (Enqueue)."""
        self.cola.append(documento)
        print(f"[ENVÍO] '{documento.nombre}' ({documento.tamano} págs) se agregó a la cola.")

    def imprimir_siguiente(self):
        """
        Toma el documento del frente (Dequeue) y simula su impresión.
        """
        if not self.cola:
            print("[INFO] La cola de impresión está vacía. La impresora está inactiva.")
            return None

        # FIFO: El primer documento en entrar, sale primero
        documento_a_imprimir = self.cola.popleft() 
        
        print(f"\n[IMPRIMIENDO] Iniciando impresión de {documento_a_imprimir.nombre} ({documento_a_imprimir.tamano} págs)...")
        
        # Simulación del tiempo de impresión
        tiempo_simulado = documento_a_imprimir.tamano * 0.1
        time.sleep(tiempo_simulado) # Pausa el programa
        
        print(f"[TERMINADO] '{documento_a_imprimir.nombre}' se ha impreso exitosamente en {tiempo_simulado:.2f} segundos.")
        
        return documento_a_imprimir

    def mostrar_estado(self):
        """Muestra los documentos restantes en la cola."""
        if not self.cola:
            print("\n>>> Cola de impresión actual: Vacía.")
        else:
            documentos_restantes = [doc.nombre for doc in self.cola]
            print(f"\n>>> Cola de impresión actual ({len(self.cola)} documentos): {documentos_restantes}")
        print("-" * 50)

# --- Simulación de uso ---
impresora = ColaImpresion()

# 1. Los usuarios envían documentos
doc1 = Documento("Informe Mensual", 15)
doc2 = Documento("Presentación de Ventas", 5)
doc3 = Documento("Factura Urgente", 1)

impresora.enviar_documento(doc1) # Llega primero
impresora.enviar_documento(doc2) # Llega segundo
impresora.enviar_documento(doc3) # Llega tercero (aunque sea urgente, debe esperar)

impresora.mostrar_estado()

# 2. La impresora comienza a trabajar (FIFO)
print("\n--- INICIO DE PROCESAMIENTO FIFO ---")
impresora.imprimir_siguiente() # Debe ser el Informe Mensual (15 págs)
impresora.mostrar_estado()

impresora.imprimir_siguiente() # Debe ser la Presentación de Ventas (5 págs)
impresora.mostrar_estado()

impresora.imprimir_siguiente() # Debe ser la Factura Urgente (1 pág)
impresora.mostrar_estado()

# 3. La impresora se queda inactiva
impresora.imprimir_siguiente()
