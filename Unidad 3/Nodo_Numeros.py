def contar_elementos(self):
    apuntador = self.root
    cuenta = 0
    while apuntador is not None:
        cuenta = cuenta + 1
        apuntador = apuntador.siguiente
    return cuenta
