
from fastapi import FastAPI
from app.api.routes.analysis import router as analysis_router

app = FastAPI(title="AI Trading Backend")

app.include_router(analysis_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "ok"}
