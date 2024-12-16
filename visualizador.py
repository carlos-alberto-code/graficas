from typing import Literal
from charts.chart_strategy import ChartStrategy


class Visualizador():
    def __init__(self, nombre_archivo: str, tipo_grafica: ChartStrategy) -> None:
        self._nombre_archivo = nombre_archivo
        self._tipo_grafica = tipo_grafica
