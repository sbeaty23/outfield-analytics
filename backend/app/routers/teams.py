from fastapi import APIRouter, Query, Path, HTTPException

teams = {
    147: "New York Yankees",
    111: "Boston Red Sox",
    119: "Los Angeles Dodgers"
}


router = APIRouter(prefix="/api/teams", tags=["teams"])
@router.get("/{team_id}")


def get_team(
    team_id: int = Path(ge=1), 
    season: int = Query(default=2025, ge=1901, le=2026)
    ):
    if team_id not in teams:
        raise HTTPException(
            status_code=404,
            detail="Team not found"
        )

    return {
        "team_id": team_id,
        "name": teams[team_id],
        "season": season
    }