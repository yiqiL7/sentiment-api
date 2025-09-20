# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from app.model import predict as predict_fn
import time, logging

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

class InferenceItem(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")

class InferenceBatch(BaseModel):
    texts: List[str]

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}

@app.post("/predict")
def predict_single(item: InferenceItem) -> Dict[str, Any]:
    return predict_fn(item.text)

@app.post("/predict_batch")
def predict_batch(items: InferenceBatch) -> List[Dict[str, Any]]:
    return [predict_fn(t) for t in items.texts]

logger = logging.getLogger("uvicorn")

@app.middleware("http")
async def timing(req, call_next):
    t0 = time.time()
    resp = await call_next(req)
    logger.info("%s %s -> %s in %.1fms", req.method, req.url.path, resp.status_code, (time.time()-t0)*1000)
    return resp

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API!"}
