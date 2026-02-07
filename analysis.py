
from fastapi import APIRouter, UploadFile, File
from app.services.vision_service import analyze_chart

router = APIRouter()

@router.post("/analyze/chart")
async def analyze_chart_endpoint(image: UploadFile = File(...)):
    return analyze_chart(image)
