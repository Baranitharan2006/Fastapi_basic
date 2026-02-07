from fastapi import FastAPI
from config import settings

app = FastAPI()


@app.get("/info")
def get_info():
    return {
        "debug": settings.debug,
        "database_url": settings.database_url,
    }
