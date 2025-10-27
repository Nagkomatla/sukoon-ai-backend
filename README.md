# Sukoon AI Backend

FastAPI server for the Sukoon Agentic AI (Schizophrenia Care Assistant).

## Project Structure

```
Builathon_nxtwave/
├── sukoon_api.py      # Main FastAPI application
├── requirements.txt   # Python dependencies
├── Procfile           # Deployment configuration for Render/Heroku
└── README.md          # Project documentation
```

## Setup

1. Install dependencies:
```bash
cd Builathon_nxtwave
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn sukoon_api:app --reload
```

## Deployment

This project includes a Procfile for deployment on platforms like Render or Heroku.

The server runs on port 10000 when deployed.

## API Endpoints

- `GET /` - Home endpoint

