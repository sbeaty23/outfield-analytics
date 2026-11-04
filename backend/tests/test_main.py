
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() ==  {
        "name": "Outfield Analytics",
        "description": "MLB statistics and predictions API"
}



def test_team_not_found():
    response = client.get("/api/teams/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Team not found"}


@pytest.mark.parametrize(
        "team_id",
        [0, -1, -5, "hello"]
)
def test_invalid_team_id(team_id):
    response = client.get(f"/api/teams/{team_id}")

    assert response.status_code == 422
    assert "detail" in response.json()


@pytest.mark.parametrize(
        "team_id, expected_name",
        [
            (147, "New York Yankees"),
            (111, "Boston Red Sox"),
            (119, "Los Angeles Dodgers")
        ]
)
def test_valid_team(team_id, expected_name):
    response = client.get(f"/api/teams/{team_id}")

    assert response.status_code == 200
    assert response.json()["team_id"] == team_id
    assert response.json()["name"] == expected_name