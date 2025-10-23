class GrafoRutas:
    """
    Representa un mapa de rutas usando una Lista de Adyacencia.
    Implementa un método para encontrar todos los caminos posibles entre dos nodos.
    """
    def __init__(self, grafo):
        # El grafo se representa como un diccionario (Lista de Adyacencia)
        self.grafo = grafo

    def encontrar_todos_los_caminos(self, origen, destino):
        """Función principal para encontrar todos los caminos."""
        
        if origen not in self.grafo or destino not in self.grafo:
            return "Error: Origen o destino no existen en el mapa."

        todos_los_caminos = []
        # La lista 'camino_actual' rastrea la ruta tomada en la recursión
        camino_actual = []
        
        self._dfs_backtracking(origen, destino, camino_actual, todos_los_caminos)
        
        return todos_los_caminos

    def _dfs_backtracking(self, nodo_actual, destino, camino_actual, todos_los_caminos):
        """
        Función recursiva que utiliza DFS y Backtracking.
        """
        
        # 1. Añadir el nodo actual al camino
        camino_actual.append(nodo_actual)

        # 2. Caso base: Si el nodo actual es el destino
        if nodo_actual == destino:
            # Se encontró un camino. Se añade una COPIA inmutable del camino a la lista de resultados
            todos_los_caminos.append(list(camino_actual))
        else:
            # 3. Paso recursivo: Explorar vecinos
            for vecino in self.grafo.get(nodo_actual, []):
                # Evitar ciclos: Solo visitar si el vecino no está ya en el camino actual
                if vecino not in camino_actual:
                    self._dfs_backtracking(vecino, destino, camino_actual, todos_los_caminos)
        
        # 4. Backtracking: Eliminar el nodo actual para explorar otras rutas
        camino_actual.pop()


# --- Simulación de uso ---

# Definición del mapa de rutas (Grafo)
mapa_rutas = {
    'CDMX': ['Puebla', 'Querétaro'],
    'Puebla': ['Veracruz', 'Oaxaca'],
    'Querétaro': ['Guadalajara'],
    'Veracruz': ['Oaxaca'],
    'Oaxaca': ['Chiapas'],
    'Guadalajara': ['Jalisco'],
    'Jalisco': ['Chiapas'],
    'Chiapas': []
}

grafo_mapa = GrafoRutas(mapa_rutas)

origen = 'CDMX'
destino = 'Chiapas'
caminos_encontrados = grafo_mapa.encontrar_todos_los_caminos(origen, destino)

print(f"--- Búsqueda de todos los caminos posibles ---")
print(f"Origen: {origen}, Destino: {destino}")
print("-" * 45)

if isinstance(caminos_encontrados, list):
    for i, camino in enumerate(caminos_encontrados):
        print(f"Camino {i+1}: {' -> '.join(camino)}")
    
    print(f"\nTotal de caminos encontrados: {len(caminos_encontrados)}")
else:
    print(caminos_encontrados)
