from typing import Literal
from charts.grafica import GraficaStrategy


class Visualizador():
    def __init__(self, nombre_archivo: str, tipo_grafica: GraficaStrategy) -> None:
        self._nombre_archivo = nombre_archivo
        self._tipo_grafica = tipo_grafica
