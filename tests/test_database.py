import unittest
from src.database import Database
import sys
from pathlib import Path

root_path = Path(__file__).parent.parent  # Поднимаемся на 2 уровня вверх (из tests/)
sys.path.append(str(root_path))

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")  # In-memory database for testing

    def test_add_transaction(self):
        self.db.add_transactions("2023-10-01", 100.0, "Food", "expense", "Groceries")
        transactions = self.db.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][2], 100.0)

if __name__ == "__main__":
    unittest.main()