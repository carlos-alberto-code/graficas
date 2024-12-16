import flet as ft
from reader import DataReader
from table import Table


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    reader = DataReader("archivos/sales_data.csv")
    table = Table(reader)
    page.add(table)

ft.app(target=main)
