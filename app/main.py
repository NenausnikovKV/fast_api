"""Simple fastApi view"""

from fastapi import FastAPI, Body, Header
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    """Root url"""
    return "Hello world"


@app.get("/hi/{who}")
def say_hi_path(who: str) -> str:
    """Path variable url"""
    return f"Hello {who}"


@app.get("/hi")
def say_hi_query_name(who: str = "me") -> str:
    """query variable url"""
    return f"Hello {who}"


@app.post("/hi_body")
def say_hi_body(
        who: str = Body(embed=True),
        other: str = Body(embed=True, default="others")
) -> str:
    """
    query variable url
    use embed for request body processing as simple json
    """
    return f"Hello {who} and {other}"


@app.post("/hi_header")
def say_hi_headers(who: str = Header()) -> str:
    return f"Hello {who}"


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
