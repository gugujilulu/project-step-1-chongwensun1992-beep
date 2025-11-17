"""
Summary functions for incomes and expenses.
"""

from typing import Iterable
from smartbudget.core.transaction import Income, Expense


def total_income(incomes: Iterable[Income]) -> float:
    """Return the total income amount."""
    return sum(item.amount for item in incomes)


def total_expenses(expenses: Iterable[Expense]) -> float:
    """Return the total expense amount (as a negative number)."""
    return sum(item.amount for item in expenses)


def budget_balance(incomes: Iterable[Income], expenses: Iterable[Expense]) -> float:
    """
    Return the overall budget balance:
    total_income + total_expenses.
    """
    return total_income(incomes) + total_expenses(expenses)
