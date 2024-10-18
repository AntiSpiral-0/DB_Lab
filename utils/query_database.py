import duckdb
from pathlib import Path

class QueryDatabase:
    def __init__(self, db_path: Path) -> None:
        self.connection = duckdb.connect(str(db_path))

    def fetch_table(self, query: str):
        return self.connection.execute(query).df()

