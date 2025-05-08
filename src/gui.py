import tkinter as tk
from tkinter import messagebox, ttk
from database import Database
from transaction import Transaction
from analytics import Analytics

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.db = Database()
        self.analytics = Analytics(self.db)

        # Форма для добавления транзакции
        tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=0, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1)

        tk.Label(root, text="Amount").grid(row=1, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        tk.Label(root, text="Category").grid(row=2, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=2, column=1)

        tk.Label(root, text="Type").grid(row=3, column=0)
        self.type_var = tk.StringVar(value="expense")
        tk.Radiobutton(root, text="Income", variable=self.type_var, value="income").grid(row=3, column=1)
        tk.Radiobutton(root, text="Expense", variable=self.type_var, value="expense").grid(row=3, column=2)

        tk.Label(root, text="Description").grid(row=4, column=0)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=4, column=1)

        tk.Button(root, text="Add Transaction", command=self.add_transaction).grid(row=5, column=0, columnspan=2)

        # Кнопки аналитики
        tk.Button(root, text="Show Summary", command=self.show_summary).grid(row=6, column=0)
        tk.Button(root, text="Plot Expenses", command=self.plot_expenses).grid(row=6, column=1)

    def add_transaction(self):
        try:
            date = self.date_entry.get()
            amount = self.amount_entry.get()
            category = self.category_entry.get()
            type_ = self.type_var.get()
            description = self.desc_entry.get()

            transaction = Transaction(date, amount, category, type_, description)
            self.db.add_transaction(date, amount, category, type_, description)
            messagebox.showinfo("Success", "Transaction added!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def show_summary(self):
        summary = self.analytics.get_summary()
        messagebox.showinfo("Summary",
            f"Total Income: {summary['total_income']:.2f}\n"
            f"Total Expense: {summary['total_expense']:.2f}\n"
            f"Balance: {summary['balance']:.2f}")

    def plot_expenses(self):
        self.analytics.plot_category_expenses()
        messagebox.showinfo("Success", "Plot saved as category_expenses.png")