from fastapi import FastAPI
from app.routers import games, teams


app = FastAPI(title="Outfield Analytics API")

app.include_router(games.router)
app.include_router(teams.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/")
def root():
    return {
  "name": "Outfield Analytics",
  "description": "MLB statistics and predictions API"
}





