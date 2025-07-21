from abc import ABC, abstractmethod
from .cola import EstructuraDatos

class Pila(EstructuraDatos):
    """Clase abstracta para implementaciones de pila (LIFO)"""
    
    @abstractmethod
    def empilar(self, elemento):
        """Añade un elemento al tope de la pila"""
        pass
    
    @abstractmethod
    def desempilar(self):
        """Remueve y retorna el elemento del tope de la pila"""
        pass
    
    @abstractmethod
    def tope(self):
        """Retorna el elemento del tope sin removerlo"""
        pass

class HistorialVentas:
    def __init__(self):
        self.items = []

    def empilar(self, item):
        self.items.append(item)

    def desempilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener(self):
        return list(reversed(self.items))