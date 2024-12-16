from reader.reader_strategy import ReaderStrategy
import pandas as pd


class DatabaseReader(ReaderStrategy):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def load(self) -> pd.DataFrame: ...
