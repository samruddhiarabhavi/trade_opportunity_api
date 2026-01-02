async def analyze_with_llm(sector: str, data: str) -> str:
    return f"""
# {sector.title()} Sector Trade Analysis (India)

## Market Overview
{data}

## Current Opportunities
- Strong domestic demand
- Government incentives
- Export growth potential

## Risks
- Market volatility
- Regulatory changes
- Global economic slowdown

## Trade Recommendation
Moderate to positive outlook for short to mid-term investments.
"""
