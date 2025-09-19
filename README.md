# sentiment-api

### Model Choice
Using **DistilBERT (SST-2)** via HuggingFace pipeline:
- Strong accuracy for sentiment; ~2× faster and smaller than BERT-base.
- **CPU-friendly** (no GPU required), good for low-cost cloud deploys.
- Cached on first call with `functools.lru_cache` to avoid reloading.
