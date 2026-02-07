
from pydantic import BaseModel
from typing import List

class ChartAnalysis(BaseModel):
    trend: str
    market_structure: str
    support_zones: List[float]
    resistance_zones: List[float]
    breakout_status: str
    indicator_observations: List[str]
    volatility_level: str
    summary_explanation: str
