from readers import ExcelReader, CSVReader


try:
    excel_reader = ExcelReader("archivos/game_stats.xlsx")
    df_excel = excel_reader.load()
    print("Datos Excel:", df_excel.head())
except ValueError as e:
    print(f"Error en la lectura: {e}")


try:
    csv_reader = CSVReader("archivos/sales_data.csv")
    df_csv = csv_reader.load()
    print("Datos CSV:", df_csv.head())
except ValueError as e:
    print(f"Error en la lectura: {e}")
