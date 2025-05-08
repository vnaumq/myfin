import unittest
import sys
import os
from unittest.mock import patch, MagicMock
import tkinter as tk

# Добавляем корневую директорию проекта в sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.gui import FinanceApp

class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        # Создаем тестовое окно Tk
        self.root = tk.Tk()
        # Инициализируем FinanceApp
        self.app = FinanceApp(self.root)

    def tearDown(self):
        # Уничтожаем окно после каждого теста
        self.root.destroy()

    @patch('src.gui.Database')
    @patch('src.gui.Transaction')
    @patch('src.gui.messagebox')
    def test_add_transaction_success(self, mock_messagebox, mock_transaction, mock_database):
        # Настраиваем заглушки
        mock_transaction_instance = MagicMock()
        mock_transaction.return_value = mock_transaction_instance
        mock_db_instance = MagicMock()
        mock_database.return_value = mock_db_instance

        # Устанавливаем значения в поля ввода
        self.app.date_entry.insert(0, "2023-10-01")
        self.app.amount_entry.insert(0, "100.0")
        self.app.category_entry.insert(0, "Food")
        self.app.type_var.set("expense")
        self.app.desc_entry.insert(0, "Groceries")

        # Вызываем метод
        self.app.add_transaction()

        # Проверяем, что Transaction был создан с правильными аргументами
        mock_transaction.assert_called_once_with("2023-10-01", "100.0", "Food", "expense", "Groceries")

        # Проверяем, что Database.add_transaction был вызван
        mock_db_instance.add_transaction.assert_called_once_with("2023-10-01", "100.0", "Food", "expense", "Groceries")

        # Проверяем, что messagebox.showinfo был вызван
        mock_messagebox.showinfo.assert_called_once_with("Success", "Transaction added!")

    @patch('src.gui.Database')
    @patch('src.gui.Transaction')
    @patch('src.gui.messagebox')
    def test_add_transaction_invalid_date(self, mock_messagebox, mock_transaction, mock_database):
        # Настраиваем заглушку для Transaction, чтобы она вызывала ValueError
        mock_transaction.side_effect = ValueError("Invalid date format")

        # Устанавливаем значения в поля ввода с некорректной датой
        self.app.date_entry.insert(0, "2023-13-01")
        self.app.amount_entry.insert(0, "100.0")
        self.app.category_entry.insert(0, "Food")
        self.app.type_var.set("expense")
        self.app.desc_entry.insert(0, "Groceries")

        # Вызываем метод
        self.app.add_transaction()

        # Проверяем, что messagebox.showerror был вызван
        mock_messagebox.showerror.assert_called_once_with("Error", "Invalid date format")

        # Проверяем, что Database.add_transaction НЕ был вызван
        mock_database.return_value.add_transaction.assert_not_called()

    @patch('src.gui.Analytics')
    @patch('src.gui.messagebox')
    def test_show_summary(self, mock_messagebox, mock_analytics):
        # Настраиваем заглушку для Analytics.get_summary
        mock_analytics_instance = MagicMock()
        mock_analytics.return_value = mock_analytics_instance
        mock_analytics_instance.get_summary.return_value = {
            "total_income": 1000.0,
            "total_expense": 500.0,
            "balance": 500.0
        }

        # Вызываем метод
        self.app.show_summary()

        # Проверяем, что Analytics.get_summary был вызван
        mock_analytics_instance.get_summary.assert_called_once()

        # Проверяем, что messagebox.showinfo был вызван с правильным текстом
        mock_messagebox.showinfo.assert_called_once_with(
            "Summary",
            "Total Income: 1000.00\nTotal Expense: 500.00\nBalance: 500.00"
        )

    @patch('src.gui.Analytics')
    @patch('src.gui.messagebox')
    def test_plot_expenses(self, mock_messagebox, mock_analytics):
        # Настраиваем заглушку для Analytics
        mock_analytics_instance = MagicMock()
        mock_analytics.return_value = mock_analytics_instance

        # Вызываем метод
        self.app.plot_expenses()

        # Проверяем, что Analytics.plot_category_expenses был вызван
        mock_analytics_instance.plot_category_expenses.assert_called_once()

        # Проверяем, что messagebox.showinfo был вызван
        mock_messagebox.showinfo.assert_called_once_with("Success", "Plot saved as category_expenses.png")

if __name__ == "__main__":
    unittest.main()