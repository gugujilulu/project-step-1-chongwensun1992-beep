"""
Analysis helpers for SmartBudget.
Provides simple income/expense details and sorting.
"""

from typing import Iterable, List
from smartbudget.core.transaction import Expense, Income


# ============================
# expense
# ============================

def expense_details(expenses: Iterable[Expense]) -> List[str]:
    """
    Return a list of formatted expense descriptions.
    """
    return [e.describe() for e in expenses]


def largest_expenses(expenses: Iterable[Expense], n: int = 3) -> List[Expense]:
    """
    Return the top N largest expenses by absolute amount.
    """
    return sorted(expenses, key=lambda x: abs(x.amount), reverse=True)[:n]


# ============================
# income
# ============================

def income_details(incomes: Iterable[Income]) -> List[str]:
    """
    Return a list of formatted income descriptions.
    """
    return [i.describe() for i in incomes]


def largest_incomes(incomes: Iterable[Income], n: int = 3) -> List[Income]:
    """
    Return the top N largest incomes.
    """
    return sorted(incomes, key=lambda x: x.amount, reverse=True)[:n]


# ============================
# print
# ============================

def print_records(title: str, records: Iterable):
    """
    Utility: print a list of records (either income or expenses).
    """
    print(f"\n=== {title} ===")
    if not records:
        print("No records.\n")
        return

    for r in records:
        print(" -", r.describe())
    print()
