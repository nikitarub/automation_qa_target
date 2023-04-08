from backend import app
import uvicorn
import asyncio


async def run_webhook():
    config = uvicorn.Config(app, port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

asyncio.run(run_webhook())