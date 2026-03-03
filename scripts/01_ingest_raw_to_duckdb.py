
import duckdb
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "warehouse.duckdb"

def main():
    con = duckdb.connect(DB)
    print("DuckDB initialized")
    con.close()

if __name__ == "__main__":
    main()
