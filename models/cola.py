from abc import ABC, abstractmethod

class EstructuraDatos(ABC):
    """Clase abstracta base para estructuras de datos"""
    
    @abstractmethod
    def esta_vacia(self):
        """Verifica si la estructura está vacía"""
        pass
    
    @abstractmethod
    def obtener(self):
        """Obtiene todos los elementos de la estructura"""
        pass

class Cola(EstructuraDatos):
    """Clase abstracta para implementaciones de cola (FIFO)"""
    
    @abstractmethod
    def encolar(self, elemento):
        """Añade un elemento al final de la cola"""
        pass
    
    @abstractmethod
    def desencolar(self):
        """Remueve y retorna el primer elemento de la cola"""
        pass

class ColaBoletos:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener(self):
        return list(self.items)