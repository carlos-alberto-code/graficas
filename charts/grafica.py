from abc import ABC, abstractmethod


class GraficaStrategy(ABC):
    def __init__(self, estrategia_de_archivo) -> None:
        super().__init__()

    @abstractmethod
    def graficar(self, datos):
        pass
