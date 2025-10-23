# Ejercicio 1: Implementar una pila con lista 
class Pila: 
def __init__(self): 
self.items = [] 
def push(self, dato): 
self.items.append(dato) 
def pop(self): 
return self.items.pop() if not self.is_empty() else None 
def peek(self): 
return self.items[-1] if not self.is_empty() else None 
def is_empty(self): 
return len(self.items) == 0 
# Prueba 
p = Pila() 
p.push(10) 
p.push(20) 
print(p.pop())   
# 20 
print(p.peek())  # 10 
