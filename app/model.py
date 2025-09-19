# app/model.py
from functools import lru_cache
from typing import Dict
import os
from transformers import pipeline

# Allow overriding via env var if you experiment with other models later
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "distilbert-base-uncased-finetuned-sst-2-english"
)

@lru_cache(maxsize=1)
def get_pipeline():
    """
    Load the HF sentiment pipeline once per process.
    lru_cache ensures the model downloads/loads only on the first call
    (faster subsequent inferences and safer in web servers).
    """
    return pipeline("sentiment-analysis", model=MODEL_NAME)

def predict(text: str) -> Dict[str, float | str]:
    """
    Single-text inference helper.
    Returns: {"label": "POSITIVE"|"NEGATIVE", "score": float}
    """
    clf = get_pipeline()
    out = clf(text)[0]
    return {"label": out["label"], "score": float(out["score"])}
