class ProcesadorTexto:
    """
    Clase utilitaria para formatear datos de texto.
    Simula una operación de preparación de datos antes de la inserción 
    en una estructura (Pila, Cola, o Grafo).
    """
    def __init__(self):
        # En esta clase no se requiere inicializar una estructura de datos
        pass

    def capitalizar_primera_letra(self, texto):
        """
        Convierte la primera letra de cada palabra de una cadena a mayúscula.
        
        Args:
            texto (str): La cadena de texto a formatear.
        
        Returns:
            str: La cadena con la capitalización aplicada.
        """
        if not texto:
            return ""
            
        # El método title() de Python hace esto de forma nativa.
        # Lo implementaremos de forma manual para fines demostrativos.
        
        resultado = []
        # Dividir la cadena en palabras usando espacios como delimitador.
        palabras = texto.split()
        
        for palabra in palabras:
            # Asegurarse de que la palabra no esté vacía
            if palabra:
                # La primera letra se convierte a mayúscula
                primera_letra = palabra[0].upper()
                # El resto de la palabra se mantiene en el formato original (o minúsculas)
                resto_palabra = palabra[1:].lower()
                
                resultado.append(primera_letra + resto_palabra)
        
        # Unir las palabras de nuevo en una sola cadena, separadas por un espacio
        return " ".join(resultado)

# --- Simulación de uso ---
procesador = ProcesadorTexto()

# Ejemplo 1: Nombres de clientes para una Cola
nombre_cliente = "juan perez rodriguez"
nombre_formateado = procesador.capitalizar_primera_letra(nombre_cliente)
print(f"Original (Cliente): '{nombre_cliente}'")
print(f"Formateado: '{nombre_formateado}'")
print("-" * 40)

# Ejemplo 2: Nombres de nodos para un Grafo
nombre_nodo = "ciudad de mexico"
nodo_formateado = procesador.capitalizar_primera_letra(nombre_nodo)
print(f"Original (Nodo): '{nombre_nodo}'")
print(f"Formateado: '{nodo_formateado}'")
print("-" * 40)
