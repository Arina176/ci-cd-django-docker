from typing import Iterable
import re


def calculate_balance(incomes: Iterable[float], expenses: Iterable[float]) -> float:
    """Простая функция: сумма доходов минус сумма расходов."""
    total_income = sum(incomes)
    total_expenses = sum(expenses)
    return total_income - total_expenses


def parse_amounts(text: str) -> list[float]:
    """Парсим строку с суммами в список чисел.

    Поддерживаем:
    - разделители между числами: пробел, запятая, точка с запятой
    - десятичную запятую внутри числа: 2500,5 -> 2500.5
    """
    text = text.strip()
    if not text:
        return []

    # Сначала заменяем ; на пробел (точка с запятой — разделитель чисел)
    normalized = text.replace(";", " ")

    # Запятая между цифрами — это десятичный разделитель: 2500,5 -> 2500.5
    normalized = re.sub(r"(\d),(?=\d)", r"\1.", normalized)

    # Оставшиеся запятые считаем разделителями между числами
    normalized = normalized.replace(",", " ")

    parts = normalized.split()
    values: list[float] = []

    for part in parts:
        values.append(float(part))

    return values
