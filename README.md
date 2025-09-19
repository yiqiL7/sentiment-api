# sentiment-api

### Model Choice
Using **DistilBERT (SST-2)** via HuggingFace pipeline:
- Strong accuracy for sentiment; ~2× faster and smaller than BERT-base.
- **CPU-friendly** (no GPU required), good for low-cost cloud deploys.
- Cached on first call with `functools.lru_cache` to avoid reloading.

### API Endpoints
- `GET /health` → `{"status":"ok"}`
- `POST /predict` → body `{"text":"..."}`
- `POST /predict_batch` → body `{"texts":["...","..."]}`

Run locally:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# visit http://127.0.0.1:8000/docs
