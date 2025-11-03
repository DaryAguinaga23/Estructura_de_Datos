class Nodo: 
    def __init__(self, dato): 
        self.dato = dato 
        self.siguiente = None  
 
class ListaCircular: 
    def __init__(self): 
        self.cabeza = None 
 
    def agregar(self, dato): 
        nuevo_nodo = Nodo(dato) 
        if not self.cabeza: 
            self.cabeza = nuevo_nodo 
            self.cabeza.siguiente = self.cabeza  
        else: 
            actual = self.cabeza 
            while actual.siguiente != self.cabeza: 
                actual = actual.siguiente 
            actual.siguiente = nuevo_nodo 
            nuevo_nodo.siguiente = self.cabeza 
 
    def mostrar(self): 
        if not self.cabeza: 
            print("La lista está vacía.") 
            return 
        actual = self.cabeza 
        while True: 
            print(actual.dato, end=" -> ") 
            actual = actual.siguiente 
            if actual == self.cabeza: 
                break 
        print("(circular)") 
 
    def buscar(self, dato):
        if not self.cabeza:
            return False
        actual = self.cabeza
        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    def eliminar(self, dato):
        if not self.cabeza:
            print("La lista está vacía.")
            return False
        
        # Si la lista tiene un solo nodo
        if self.cabeza.siguiente == self.cabeza:
            if self.cabeza.dato == dato:
                self.cabeza = None
                return True
            else:
                return False
        
        # Si el nodo a eliminar es la cabeza
        if self.cabeza.dato == dato:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
            return True
        
        # Buscar el nodo a eliminar
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        
        return False

    def test_lista_circular(self, datos): 
        print("=== Pruebas de Lista Circular ===") 
        print("Agregando datos:", datos) 
        for dato in datos: 
            self.agregar(dato) 
        print("Lista después de agregar los datos:") 
        self.mostrar() 
        print("=== Fin de las Pruebas ===") 

def menu():
    lista = ListaCircular()
    
    while True:
       
        print("MENÚ - LISTA CIRCULAR TECNM")
       
        print("1. Añadir dato")
        print("2. Buscar dato")
        print("3. Eliminar dato")
        print("4. Mostrar lista")
        print("5. Salir")
      
        
        op = input("Selecciona una opción (1-5): ")
        
        if op == "1":
            try:
                cant = int(input("¿Cuántos valores deseas agregar? "))
                for i in range(cant):
                    valor = int(input(f"Ingresa el valor {i+1}: "))
                    lista.agregar(valor)
                print(f" {cant} valor(es) añadido(s) correctamente.")
            except ValueError:
                print(" Error: Debes ingresar un número entero.")
        
        elif op == "2":
            try:
                dato = int(input("Ingresa el valor a buscar: "))
                if lista.buscar(dato):
                    print(f" El valor {dato} SÍ está en la lista.")
                else:
                    print(f" El valor {dato} NO está en la lista.")
            except ValueError:
                print(" Error: Debes ingresar un número entero.")
        
        elif op == "3":
            try:
                dato = int(input("Ingresa el valor a eliminar: "))
                if lista.eliminar(dato):
                    print(f" Valor {dato} eliminado correctamente.")
                else:
                    print(f" El valor {dato} no se encontró en la lista.")
            except ValueError:
                print(" Error: Debes ingresar un número entero.")
        
        elif op == "4":
            print("\nLista actual:")
            lista.mostrar()
        
        elif op == "5":
            print("\n¡Hasta luego!")
            break
        
        else:
            print(" Opción inválida. Por favor selecciona una opción del 1 al 5.")
menu()
