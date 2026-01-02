"# trade_opportunity_api" 
## Description
FastAPI service that analyzes Indian market sectors and returns trade opportunity reports in Markdown format.

## Tech Stack
- FastAPI
- Rate Limiting (SlowAPI)
- API Key Authentication
- In-memory storage
- LLM-based analysis (mocked)

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
