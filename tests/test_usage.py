"""
Test file for SmartBudget package.
This script demonstrates how to use major features of the package.
Run it independently to validate functionality.
"""

from smartbudget.entity.transaction import Income, Expense
from smartbudget.analysis.summary import (
    total_income,
    total_expenses,
    budget_balance,
)
from smartbudget.analysis.insights import (
    expense_details,
    income_details,
)
from smartbudget.io import save_to_json, load_from_json, list_files, delete_file


def run_tests():
    print("\n============================")
    print("=== TEST 1: Creating Records ===")
    print("============================\n")

    incomes = [
        Income("Salary", 5000, "Company A"),
        Income("Bonus", 1200, "Company A"),
    ]

    expenses = [
        Expense("Rent", 1500, "Housing"),
        Expense("Groceries", 400, "Food"),
        Expense("Internet", 90, "Utilities"),
    ]

    for i in incomes:
        print("Income:", i.describe())

    for e in expenses:
        print("Expense:", e.describe())




def main():
    print("\n=== Running SmartBudget Test Suite ===")
    run_tests()


if __name__ == "__main__":
    main()
