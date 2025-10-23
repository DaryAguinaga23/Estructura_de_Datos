# Ejercicio 3: Implementar un grafo con lista de adyacencia 
class Grafo: 
def __init__(self): 
self.ady = {} 
def agregar_vertice(self, v): 
if v not in self.ady: 
self.ady[v] = [] 
def agregar_arista(self, v1, v2): 
if v1 in self.ady and v2 in self.ady: 
self.ady[v1].append(v2) 
self.ady[v2].append(v1)  # Si es no dirigido 
def mostrar(self): 
for v in self.ady: 
print(v, "->", self.ady[v]) 
# Prueba 
g = Grafo() 
for v in ["A", "B", "C", "D"]: 
g.agregar_vertice(v) 
g.agregar_arista("A", "B") 
g.agregar_arista("A", "C") 
g.agregar_arista("B", "D") 
g.mostrar() 
