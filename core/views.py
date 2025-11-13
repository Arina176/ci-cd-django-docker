from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .utils import calculate_balance, parse_amounts


def index(request: HttpRequest) -> HttpResponse:
    result = None
    error = None
    total_incomes = 0.0
    total_expenses = 0.0

    incomes_input = ""
    expenses_input = ""

    if request.method == "POST":
        incomes_input = request.POST.get("incomes", "")
        expenses_input = request.POST.get("expenses", "")

        try:
            incomes = parse_amounts(incomes_input)
            expenses = parse_amounts(expenses_input)
            total_incomes = sum(incomes)
            total_expenses = sum(expenses)
            result = calculate_balance(incomes, expenses)
        except ValueError:
            error = "Не получилось разобрать числа. Проверь, что введены только суммы (например: 1000, 2500.5, 300)."

    context = {
        "result": result,
        "error": error,
        "total_incomes": total_incomes,
        "total_expenses": total_expenses,
        "incomes_input": incomes_input,
        "expenses_input": expenses_input,
    }
    return render(request, "core/index.html", context)