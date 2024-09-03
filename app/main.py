"""Simple fastApi view"""

from fastapi import FastAPI
import uvicorn

from app.routers import greeting, product
from app.routers.tags import TAGS_METADATA, Tags

app = FastAPI(
    title="Hello app",
    description="Say hello to everyone",
    summary="Simple app",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "anon",
        "email": "spam_box@example.com"
    },
    license_info={
        "name": "no license"
    },
    openapi_tags=TAGS_METADATA
)
app.include_router(greeting.router)
app.include_router(product.router)


@app.get("/", tags=[Tags.ROOT])
def root():
    """Root url"""
    return "Root page"


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
