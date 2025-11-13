FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

# Системные зависимости (по минимуму)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости приложения
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Переменная окружения по умолчанию (порт)
ENV PORT=8000

# Команда запуска: применяем миграции и стартуем gunicorn
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn mysite.wsgi:application --bind 0.0.0.0:${PORT}"]