"""hello routers"""

from fastapi import Body, Header, APIRouter

from app.routers.tags import Tags


router = APIRouter()


@router.get(
    "/hi",
    tags=[Tags.GREETING],
    summary="say hello world",
    description="simple root router method which return one constant line",
    response_description="returned constant base greeting",
    response_model=str,
    operation_id="hi",
    deprecated=False
)
def say_hi():
    """root router path"""
    return "Hello world"


@router.get("/hi/path/{who}", tags=[Tags.GREETING])
def say_hi_path(who: str) -> str:
    """Path variable url"""
    return f"Hello {who}"


@router.get("/hi/query", tags=[Tags.GREETING])
def say_hi_query_name(who: str = "me") -> str:
    """query variable url"""
    return f"Hello {who}"


@router.post("/hi/body", tags=[Tags.GREETING])
def say_hi_body(
        who: str = Body(embed=True),
        other: str = Body(embed=True, default="others")
) -> str:
    """
    query variable url
    use embed for request body processing as simple json
    """
    return f"Hello {who} and {other}"


@router.post("/hi/header", tags=[Tags.GREETING])
def say_hi_headers(who: str = Header()) -> str:
    """Headers variable url"""
    return f"Hello {who}"
