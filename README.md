# MYFIN

## Личный финансовый трекер на Python

### Описание

Приложение для отслеживания доходов и расходов, анализа бюджета и визуализации финансовых данных. Оно позволит пользователям добавлять транзакции, категоризировать их, просматривать статистику и получать визуальные отчеты.


### Библиотеки:
sqlite3 — для хранения данных (встроенная база данных).
pandas — для анализа данных.
matplotlib и seaborn — для визуализации.
tkinter — для графического интерфейса (GUI).

### Инструменты:
uv

### Структура проекта
personal_finance_tracker/
│
├── src/                     # Исходный код
│   ├── __init__.py          # Пустой файл для обозначения пакета
│   ├── main.py              # Точка входа в приложение
│   ├── database.py          # Логика работы с базой данных
│   ├── transaction.py       # Класс для работы с транзакциями
│   ├── analytics.py         # Логика анализа и статистики
│   └── gui.py               # Графический интерфейс
│
├── data/                    # Данные
│   └── finance.db           # SQLite база данных
│
├── tests/                   # Тесты
│   ├── __init__.py
│   ├── test_database.py     # Тесты для базы данных
│   ├── test_transaction.py  # Тесты для транзакций
│   └── test_analytics.py    # Тесты для аналитики
│
├── requirements.txt         # Зависимости проекта
├── README.md               # Описание проекта
└── .gitignore              # Игнорируемые файлы

### Подробный план действий

1. Подготовка окружения

Установите зависимости: Создайте файл requirements.txt:

pandas==2.2.3
matplotlib==3.9.2
seaborn==0.13.2

Установите их:

pip install -r requirements.txt

tkinter встроен в Python, поэтому устанавливать его не нужно.

2. Настройка структуры проекта





Создайте папки и файлы, как указано в структуре выше.



Добавьте .gitignore:

__pycache__/
*.pyc
venv/
*.db

3. Разработка базы данных (database.py)

Создайте базу данных SQLite для хранения транзакций.

 import sqlite3 from datetime import datetime

class Database: def init(self, db_name="data/finance.db"): self.conn = sqlite3.connect(db_name) self.create_tables()

def create_tables(self):
    with self.conn:
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT
            )
        """)

def add_transaction(self, date, amount, category, type_, description):
    with self.conn:
        self.conn.execute("""
            INSERT INTO transactions (date, amount, category, type, description)
            VALUES (?, ?, ?, ?, ?)
        """, (date, amount, category, type_, description))

def get_transactions(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()

def __del__(self):
    self.conn.close()