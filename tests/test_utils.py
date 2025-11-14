import math

from core.utils import calculate_balance, parse_amounts


def test_calculate_balance_positive():
    incomes = [1000, 2000, 500]
    expenses = [300, 700]
    assert calculate_balance(incomes, expenses) == 2500


def test_calculate_balance_negative():
    incomes = [1000]
    expenses = [800, 500]
    assert calculate_balance(incomes, expenses) == -300


def test_parse_amounts_empty():
    assert parse_amounts("") == []
    assert parse_amounts("   ") == []


def test_parse_amounts_commas_and_semicolons():
    text = "1000, 2000; 300.5"
    values = parse_amounts(text)
    assert len(values) == 3
    assert math.isclose(values[0], 1000.0)
    assert math.isclose(values[1], 2000.0)
    assert math.isclose(values[2], 300.5)


def test_parse_amounts_spaces_and_comma_decimals():
    text = "1000  2500,5  300"
    values = parse_amounts(text)
    assert len(values) == 3
    # 2500,5 -> 2500.5
    assert math.isclose(values[1], 2500.5)
