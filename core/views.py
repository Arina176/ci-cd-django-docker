from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Привет, CI/CD + Docker!</h1><p>Это прод-сервер.</p>")