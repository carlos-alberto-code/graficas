import flet as ft
from reader import DataReader
from table import Table, create_rows


reader = DataReader("archivos/sales_data.csv")
create_rows(reader)
# def main(page: ft.Page):
#     page.theme_mode = ft.ThemeMode.LIGHT

#     table = Table(reader)
#     page.add(table)

# ft.app(target=main)
