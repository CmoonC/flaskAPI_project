from fastapi import FastAPI

app = FastAPI()

#Running a health check
@app.get("/")
def health_check():
    return {"status_code": 200,
            "detail": "ok",
            "result": "working"}


