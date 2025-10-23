# Ejercicio 2: Implementar una cola con lista 
class Cola: 
def __init__(self): 
self.items = [] 
def enqueue(self, dato): 
self.items.append(dato) 
def dequeue(self): 
return self.items.pop(0) if not self.is_empty() else None 
def front(self): 
return self.items[0] if not self.is_empty() else None 
def is_empty(self): 
return len(self.items) == 0 
# Prueba 
c = Cola() 
c.enqueue("A") 
c.enqueue("B") 
c.enqueue("C") 
print(c.dequeue())  # A 
print(c.front())    
# B 
