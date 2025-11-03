def __len__(self): 
    cur, c = self.head, 0 
    while cur: c += 1; cur = cur.next 
    return c 
 
def k_from_end(self, k): 
    # usando tail y prev: 
    cur = self.tail 
    i = 1 
    while cur and i < k: 
        cur = cur.prev; i += 1 
    return cur.dato if cur else None
