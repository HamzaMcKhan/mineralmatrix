from fastapi import FastAPI

app = FastAPI(title="mineralmatrix")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
