import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.mark.parametrize(
    "game_id, expected_home, expected_away",
    [
      (101, "New York Yankees",	"Boston Red Sox"),
      (102,	"Los Angeles Dodgers", "New York Yankees") 
    ]
)
def test_valid_game(game_id, expected_home, expected_away):
    response = client.get(f"/api/games/{game_id}")

    assert response.status_code == 200
    assert response.json()["home_team"] == expected_home
    assert response.json()["away_team"] == expected_away


def test_game_not_found():
    response = client.get("/api/games/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Game not found"
        }


@pytest.mark.parametrize(
    "game_id",
    [0, -1, "invalid"]
)
def test_invalid_game_id(game_id):
    response = client.get(f"/api/games/{game_id}")

    assert response.status_code == 422
    assert "detail" in response.json()

