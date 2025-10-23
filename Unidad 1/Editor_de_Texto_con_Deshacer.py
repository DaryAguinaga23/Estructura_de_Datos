class EditorSimulado:
    """
    Simula las funciones de Deshacer (Undo) y Rehacer (Redo) 
    de un editor de texto usando dos pilas (listas de Python).
    """
    def __init__(self):
        # Pila LIFO para las acciones que se pueden deshacer
        self.historial_undo = [] 
        # Pila LIFO para las acciones que se pueden rehacer
        self.historial_redo = [] 
        # El estado actual del "documento"
        self.contenido = "Documento inicial." 

    def ejecutar_accion(self, accion):
        """Simula la realización de una nueva acción (PUSH a undo)."""
        
        # 1. Guardar el estado actual ANTES de la acción en la pila de undo
        self.historial_undo.append(self.contenido)
        
        # 2. Aplicar la nueva acción y limpiar la pila de redo (ya no es válida)
        self.contenido = accion
        self.historial_redo.clear()
        print(f"-> Realizada: '{accion}'")

    def deshacer(self):
        """Revierte la última acción (POP de undo, PUSH a redo)."""
        
        if not self.historial_undo:
            print("--- No hay más acciones para deshacer. ---")
            return

        # 1. Guardar el estado actual en el historial de redo
        self.historial_redo.append(self.contenido)
        
        # 2. Recuperar el estado anterior de la pila de undo (POP)
        accion_deshecha = self.historial_undo.pop()
        self.contenido = accion_deshecha
        
        print(f"<- Deshecha. Contenido restaurado a: '{accion_deshecha}'")

    def rehacer(self):
        """Reaplica la última acción deshecha (POP de redo, PUSH a undo)."""
        
        if not self.historial_redo:
            print("--- No hay más acciones para rehacer. ---")
            return

        # 1. Guardar el estado actual en la pila de undo
        self.historial_undo.append(self.contenido)
        
        # 2. Recuperar el estado de la pila de redo (POP)
        accion_rehecha = self.historial_redo.pop()
        self.contenido = accion_rehecha
        
        print(f"-> Rehecha. Contenido actualizado a: '{accion_rehecha}'")

    def mostrar_contenido(self):
        """Muestra el estado actual del documento y las pilas."""
        print(f"\n[ESTADO] Contenido actual: '{self.contenido}'")
        print(f"  Pila UNDO (último estado): '{self.historial_undo[-1] if self.historial_undo else 'Vacía'}'")
        print(f"  Pila REDO (último estado): '{self.historial_redo[-1] if self.historial_redo else 'Vacía'}'")
        print("-" * 40)


# --- Simulación de uso ---
editor = EditorSimulado()
editor.mostrar_contenido()

# Primeras acciones
editor.ejecutar_accion("Título del documento.") 
editor.ejecutar_accion("Introducción redactada.")
editor.mostrar_contenido()

# Deshacer y Rehacer (LIFO en acción)
editor.deshacer() # Vuelve a "Título del documento."
editor.mostrar_contenido()

editor.rehacer() # Vuelve a "Introducción redactada."
editor.mostrar_contenido()

# Una nueva acción limpia la pila de REDO
editor.ejecutar_accion("Se añadió un gráfico.")
editor.mostrar_contenido()
