from typing import Iterable


def calculate_balance(incomes: Iterable[float], expenses: Iterable[float]) -> float:
    """Простая функция: сумма доходов минус сумма расходов."""
    total_income = sum(incomes)
    total_expenses = sum(expenses)
    return total_income - total_expenses
