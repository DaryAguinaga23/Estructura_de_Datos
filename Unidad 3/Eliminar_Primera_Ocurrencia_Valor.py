def remove_node(self, nodo): 
    if not nodo: return 
    if nodo.prev: nodo.prev.next = nodo.next 
    else: self.head = nodo.next 
    if nodo.next: nodo.next.prev = nodo.prev 
    else: self.tail = nodo.prev 
    nodo.prev = nodo.next = None 
 
def remove_value(self, v): 
    nodo = self.find(v) 
    self.remove_node(nodo) 
