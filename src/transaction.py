from datetime import datetime
from typing import Optional
from dateutil.parser import parse as parse_date
from src.database import Database

class Transaction:
    def __init__(self, db: Database ,id: int, amount: float, category: str, date: datetime, type: str = "", description: str = ""):
        if amount == 0:
            raise ValueError("Сумма транзакции не может быть нулевой")
        if not category.strip():
            raise ValueError("Категория не может быть пустой")
        if not isinstance(date, datetime):
            raise ValueError("Дата должна быть объектом datetime")

        self.db = db
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.type = type
        self.description = description

    @classmethod
    def from_dict(cls,db: Database, data: dict) -> 'Transaction':
        required_keys = {'id', 'amount', 'category', 'type', 'date'}
        if not all(key in data for key in required_keys):
            raise KeyError("Словарь должен содержать ключи: id, amount, category, date")

        date = parse_date(data['date']) if isinstance(data['date'], str) else data['date']

        return cls(
            db=db,
            id=data['id'],
            amount=data['amount'],
            category=data['category'],
            date=date,
            type=data.get('type'),
            description=data.get('description')
        )

    def to_dict(self) -> dict:

        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date.isoformat(),
            'type':self.type,
            'description': self.description
        }

    def save(self):
        """Сохраняет транзакцию в базе данных"""
        self.db.add_transactions(
            date=self.date.isoformat(),
            amount=self.amount,
            category=self.category,
            type=self.type,
            description=self.description
        )

    @classmethod
    def get_all(cls, db: Database) -> list['Transaction']:
        """Получает все транзакции из базы данных"""
        transactions = db.get_transactions()
        return [
            cls(
                db=db,
                id=t[0],
                date=parse_date(t[1]),
                amount=t[2],
                category=t[3],
                type=t[4],
                description=t[5] if t[5] is not None else ''
            ) for t in transactions
        ]