import os

from fastapi import FastAPI

app = FastAPI(
    title="Mein Server API",
    description="My first Dockerized FastAPI application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Mein Server läuft erfolgreich!",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/config")
def get_config():
    return {
        "app_name": os.getenv("APP_NAME", "not set"),
        "app_version": os.getenv("APP_VERSION", "not set"),
        "app_env": os.getenv("APP_ENV", "not set")
    }