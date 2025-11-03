def eliminar_elemento(self, x):
    if self.root is None:
        print("La lista esta vacia")
        return

    if self.root.siguiente is None:
        if self.root.elemento == x:
            self.root = None
        else:
            print("Elemento no encontrado")
            
    if self.root.elemento == x:
        self.eliminar_inicio()
        return

    apuntador = self.root
    while apuntador.siguiente is not None:
        if apuntador.elemento == x:
            break
        apuntador = apuntador.siguiente

    if apuntador.siguiente is not None:
        apuntador.anterior.siguiente = apuntador.siguiente
        apuntador.siguiente.anterior = apuntador.anterior
    else:
        if apuntador.elemento == x:
            self.eliminar_final()
        else:
            return print("Elemento no encontrado")
