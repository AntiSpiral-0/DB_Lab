import duckdb
import pandas as pd

class QueryDatabase:
    def __init__(self, db_path: str):
        self.connection = duckdb.connect(db_path)

    def fetch_table(self, query: str) -> pd.DataFrame:
        return self.connection.execute(query).df()
