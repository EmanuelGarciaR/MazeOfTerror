
from abc import ABC, abstractmethod

class Elemento(ABC):
    @abstractmethod
    def icon_repr(self) -> str:
        pass



class Laberinto:
    def __init__(self, n: int):
        self.n = n
        self.matriz: list[list[Elemento]] = self.generar_laberinto()
        self.salida: tuple[int, int] = None
        self.personas: list[Elemento] = []
        self.iteracion_actual: int = 0
    
    def generar_laberinto(self):
        matriz = []
        for fila in range(self.n):
            fila_actual = []
            for columna in range(self.n):
                fila_actual.append(None)
            matriz.append(fila_actual)
        return matriz