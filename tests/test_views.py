import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    url = reverse("index")
    resp = client.get(url)
    assert resp.status_code == 200
    assert "CI/CD + Docker" in resp.content.decode()


def test_health_view(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
