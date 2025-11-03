def insertar_lista_vacia(self, dato):
    if self.root is None:
        nuevoNodo = Nodo(dato)
        self.root = nuevoNodo
    else:
        print("La lista no esta vacia")
