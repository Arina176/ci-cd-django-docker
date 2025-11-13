from core.utils import calculate_balance


def test_calculate_balance_positive():
    incomes = [1000, 2000, 500]
    expenses = [300, 700]
    assert calculate_balance(incomes, expenses) == 2500


def test_calculate_balance_negative():
    incomes = [1000]
    expenses = [800, 500]
    assert calculate_balance(incomes, expenses) == -300
