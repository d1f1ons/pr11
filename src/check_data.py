import sqlite3
from pathlib import Path

db = Path(__file__).resolve().parent.parent / "db" / "shoe_store.sqlite"
conn = sqlite3.connect(db)
cur = conn.cursor()

for t in ["users", "products", "stock_items", "orders", "order_items"]:
    try:
        n = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        cols = [(c[1], c[2], "NOT NULL" if c[3] else "") for c in cur.execute(f"PRAGMA table_info({t})")]
        print(f"{t}: {n} строк")
        print("   столбцы:", cols)
    except sqlite3.OperationalError as e:
        print(f"{t}: ОШИБКА - {e}")
conn.close()