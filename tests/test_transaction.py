import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from src.transaction import Transaction
import pytest

def test_transaction_creation():
    """Тест создания объекта Transaction."""
    t = Transaction(1, 100.0, "Зарплата", datetime.now(), type="income", description="Тест")
    assert t.amount == 100.0
    assert t.type == "income"
    assert t.description == "Тест"

def test_from_dict():
    """Тест создания Transaction из словаря."""
    data = {'id': 2, 'amount': -50.0, 'category': 'Еда', 'date': '2025-05-10', 'type': 'expense', 'description': ''}
    t = Transaction.from_dict(data)
    assert t.amount == -50.0
    assert t.type == "expense"
    assert t.date.strftime('%Y-%m-%d') == '2025-05-10'