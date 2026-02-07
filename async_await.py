import httpx
import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

JOKE_URL = "https://official-joke-api.appspot.com/random_joke"


# -------------------- SYNC VERSION --------------------
@app.get("/jokes-sync")
def get_jokes_sync():
    start = time.time()
    jokes = []

    with httpx.Client() as client:
        for _ in range(10):
            resp = client.get(JOKE_URL)
            data = resp.json()
            jokes.append(f"{data['setup']} - {data['punchline']}")

    elapsed = time.time() - start

    return {
        "mode": "sync",
        "elapsed_time_sec": round(elapsed, 3),
        "jokes": jokes,
    }


# -------------------- ASYNC VERSION --------------------
@app.get("/jokes-async")
async def get_jokes_async():
    start = time.time()
    jokes = []

    async with httpx.AsyncClient() as client:
        tasks = [client.get(JOKE_URL) for _ in range(10)]
        responses = await asyncio.gather(*tasks)

        for resp in responses:
            data = resp.json()
            jokes.append(f"{data['setup']} - {data['punchline']}")

    elapsed = time.time() - start

    return {
        "mode": "async",
        "elapsed_time_sec": round(elapsed, 3),
        "jokes": jokes,
    }
