import asyncio
import uvicorn
import os

from fastapi import FastAPI

app = FastAPI(
    title=os.getenv("APP_NAME"),
    description=os.getenv("APP_DESCRIPTION"),
    version=os.getenv("APP_VERSION"),
    docs_url=os.getenv("APP_DOCS_URL"),
    redoc_url=os.getenv("APP_REDOC_URL")
)

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to ECarZ API",
        "versions": {
            "v1": "/v1",
            "v2": "/v2",
        }
    }

async def main():
    config = uvicorn.Config(
        "main:app",
        host=os.getenv("APP_HOST", "127.0.0.1"),
        port=int(os.getenv("APP_PORT", 3003)),
        log_level=os.getenv("APP_LOG_LEVEL", "info")
    )
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())