
# Outfield Analytics

A backend-focused MLB analytics and machine learning application.

**Status:** In development

## Project Overview

Outfield Analytics is a full-stack application designed to provide
MLB team information, historical statistics, and data-driven game
predictions.

The project emphasizes backend engineering, data pipelines,
relational database design, and machine learning.

## Planned Features

- MLB team, roster, and schedule information
- Team performance statistics and recent trends
- Machine learning-based game predictions
- Historical prediction evaluation
- Automated data ingestion and prediction pipelines

## Technology Stack

- Python
- FastAPI
- PostgreSQL (planned)
- SQLAlchemy (planned)
- scikit-learn (planned)
- React and TypeScript (planned)
- pytest

## Current Progress

### Phase 1: Backend Foundations — Complete

- Created the FastAPI application
- Implemented team and game endpoints using mock data
- Added path and query parameter validation
- Implemented HTTP error handling
- Organized endpoints using APIRouter
- Created automated API tests with pytest

## Running the Backend

From the backend directory:

1. Create a virtual environment:
```
py -m venv .venv
```
2. Activate the environment:
```
.\.venv\Scripts\Activate.ps1
```
3. Install dependencies:
```
python -m pip install -r requirements.txt
```
4. Start the API:
```
python -m uvicorn app.main:app --reload
```
API documentation:
http://127.0.0.1:8000/docs

## Running Tests

From the backend directory:
```
    python -m pytest -v
```
## Development Roadmap

- [x] Phase 1: Backend Foundations
- [ ] Phase 2: Database Engineering
- [ ] Phase 3: Data Engineering
- [ ] Phase 4: Backend API Development
- [ ] Phase 5: Feature Engineering
- [ ] Phase 6: Machine Learning
- [ ] Phase 7: Automated Prediction Pipeline
- [ ] Phase 8: Frontend
- [ ] Phase 9: Deployment and DevOps

## License and Data

Baseball data sources and their usage permissions will be
documented as data ingestion is implemented. The project
does not currently include live MLB data.
