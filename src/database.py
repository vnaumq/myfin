import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_name="data/finance.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT not NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT
                )
            """)

    def add_transactions(self, date:str, amount:float, category:str, type:str, description:str):
        """Добавление транзакции"""
        with self.conn:
            self.conn.execute("""
                INSERT INTO transactions (date, amount, category, type, description)
                VALUES (?, ?, ?, ?, ?)
            """, (date, amount, category, type, description))

    def get_transactions(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions")

        return cursor.fetchall()

    def __del__(self):
        self.conn.close