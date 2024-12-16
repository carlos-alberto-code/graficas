import flet as ft
from reader import DataReader


class Table(ft.DataTable):
    def __init__(self, file_path: str):
        self._file_path = file_path
        reader = DataReader(file_path)
        self._data = reader.data
        super().__init__(
             columns=[
                  ft.DataColumn(label=ft.Text(value=col_name)) for col_name in self._data.columns
             ],
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


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    table = Table("archivos/sales_data.csv")
    page.add(table)

ft.app(target=main)
