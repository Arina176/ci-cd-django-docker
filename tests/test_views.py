import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view_get(client):
    url = reverse("index")
    resp = client.get(url)
    assert resp.status_code == 200
    content = resp.content.decode()
    assert "Калькулятор личных средств" in content
    assert "Доходы" in content
    assert "Расходы" in content


@pytest.mark.django_db
def test_index_view_post_valid_data(client):
    url = reverse("index")
    data = {
        "incomes": "1000, 2000",
        "expenses": "500; 700",
    }
    resp = client.post(url, data)
    assert resp.status_code == 200
    text = resp.content.decode()

    # Доходы = 3000, расходы = 1200, остаток = 1800
    assert "Остаток: 1800.0 ₽" in text
    assert "Доходы: 3000.0 ₽" in text
    assert "Расходы: 1200.0 ₽" in text


@pytest.mark.django_db
def test_index_view_post_invalid_data(client):
    url = reverse("index")
    data = {
        "incomes": "1000, abc, 200",
        "expenses": "500",
    }
    resp = client.post(url, data)
    assert resp.status_code == 200
    text = resp.content.decode()
    assert "Не получилось разобрать числа" in text


def test_health_view(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
