from datetime import datetime
from typing import Optional
from dateutil.parser import parse as parse_date

#Класс для представления финансовой транзакции
class Transaction:
    #Инициализация новой транзакции.
    def __init__(self, id: int, amount: float, category: str, date: datetime, type: str = "", description: str = ""):
        if amount == 0:
            raise ValueError("Сумма транзакции не может быть нулевой")
        if not category.strip():
            raise ValueError("Категория не может быть пустой")
        if not isinstance(date, datetime):
            raise ValueError("Дата должна быть объектом datetime")

        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.type = type
        self.description = description

    #Создание транзакции
    @classmethod
    def from_dict(cls, data: dict) -> 'Transaction':
        required_keys = {'id', 'amount', 'category', 'type', 'date'}
        if not all(key in data for key in required_keys):
            raise KeyError("Словарь должен содержать ключи: id, amount, category, date")

        date = parse_date(data['date']) if isinstance(data['date'], str) else data['date']

        return cls(
            id=data['id'],
            amount=data['amount'],
            category=data['category'],
            date=date,
            type=data.get('type'),
            description=data.get('description')
        )

    #Преобразует транзакцию в словарь для хранения
    def to_dict(self) -> dict:

        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date.isoformat(),
            'type':self.type,
            'description': self.description
        }
