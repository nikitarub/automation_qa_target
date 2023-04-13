from fastapi import FastAPI

from routers import slow

app = FastAPI(
    title="FastAPI Interview",
    description=""
)

app.include_router(slow.router)


@app.get("/")
def hi():
    return "How are u?"
