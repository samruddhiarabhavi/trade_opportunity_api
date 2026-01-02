from fastapi import FastAPI, Depends
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.responses import PlainTextResponse
from fastapi import Request


from app.auth import verify_api_key
from app.rate_limit import limiter
from app.services.search import fetch_market_news
from app.services.llm import analyze_with_llm

app = FastAPI(title="Trade Opportunities API")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# In-memory cache (NO DB)
cache = {}

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return PlainTextResponse("Rate limit exceeded", status_code=429)


@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    api_key: str = Depends(verify_api_key)
):

    if not sector.isalpha():
        return PlainTextResponse("Invalid sector name", status_code=400)

    if sector in cache:
        return PlainTextResponse(cache[sector], media_type="text/markdown")

    market_data = await fetch_market_news(sector)
    report = await analyze_with_llm(sector, market_data)

    cache[sector] = report
    return PlainTextResponse(report, media_type="text/markdown")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0", port=8000)
