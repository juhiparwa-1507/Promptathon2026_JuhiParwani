from fastapi import FastAPI

app = FastAPI(
    title="Smart Hospital Command Center API"
)

@app.get("/")
def home():
    return {
        "message": "Backend API Running",
        "agents": [
            "Reception Agent",
            "Doctor Agent",
            "Memory Agent"
        ]
    }
