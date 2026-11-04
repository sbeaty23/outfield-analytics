from fastapi import APIRouter, Query, Path, HTTPException
games = {
    101: {
        "home_team": "New York Yankees",
        "away_team": "Boston Red Sox"
    },
    102: {
        "home_team": "Los Angeles Dodgers",
        "away_team": "New York Yankees"
    }
}


router = APIRouter(prefix="/api/games", tags=["games"])
@router.get("/{game_id}")


def get_game(
    game_id: int = Path(ge=1),
    season: int = Query(default=2025, ge=1901, le=2026)         
    ):
    if game_id not in games:
            raise HTTPException(
                status_code=404,
                detail="Game not found"
            )

    return {
        "game_id": game_id,
        "home_team": games[game_id]["home_team"],
        "away_team": games[game_id]["away_team"],
        "season": season
    }
