def remove_dups(self): 
    vistos = set() 
    cur = self.head 
    while cur: 
        if cur.dato in vistos: 
            borrar = cur 
            cur = cur.next 
            self.remove_node(borrar) 
        else: 
            vistos.add(cur.dato) 
            cur = cur.next 
