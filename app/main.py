"""Simple fastApi view"""

from fastapi import FastAPI
import uvicorn

from app.routers import greeting

app = FastAPI()
app.include_router(greeting.router)


@app.get("/", tags=["root"])
def root():
    """Root url"""
    return "Root page"


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
