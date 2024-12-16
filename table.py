import flet as ft
from reader import DataReader


def create_columns(reader: DataReader) -> list[ft.DataColumn]:
     columns = [col for col in reader.data.columns]
     return [
          ft.DataColumn(
               label=ft.Text(value=col_name),
               on_sort=lambda e: print(f"Ordenar por {e.control.label.value}")
          )
          for col_name in columns
     ]


class Table(ft.DataTable):
    def __init__(self, reader: DataReader) -> None:
        self._data = reader.data
        super().__init__(
             columns=create_columns(reader),
             rows=[
                  ft.DataRow(
                       cells=[
                            ft.DataCell(
                                 content=ft.Text(value=str(self._data.iloc[i, j])) if j != 0 else ft.Text(value=str(self._data.iloc[i, j]))
                            ) for j in range(len(self._data.columns))
                       ]
                  ) for i in range(len(self._data))
             ]
        )


