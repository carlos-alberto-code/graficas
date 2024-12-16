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


def create_rows(reader: DataReader) -> list[ft.DataRow]:
     print(reader.data.loc[1])
     return [
          ft.DataRow(
               cells=[
                    ft.DataCell(
                         content=ft.Text()
                    )
               ]
          )
     ]


class Table(ft.DataTable):
    def __init__(self, reader: DataReader) -> None:
        self._data = reader.data
        super().__init__(
             columns=create_columns(reader),
             rows=create_rows(reader)
        )




