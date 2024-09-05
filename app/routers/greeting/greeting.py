"""hello routers"""

from fastapi import Body, Header, APIRouter
from pydantic import BaseModel

from app.tags import Tags


router = APIRouter(
    prefix="/hi",
    tags=[Tags.GREETING],
    responses={404: {"description": "Not found"}}
)


@router.get(
    "/",
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


@router.get("/path/{who}", tags=[Tags.GREETING])
def say_hi_path(who: str) -> str:
    """Path variable url"""
    return f"Hello {who}"


@router.get("/query", tags=[Tags.GREETING])
def say_hi_query_name(who: str = "me") -> str:
    """query variable url"""
    return f"Hello {who}"


@router.post("/body", tags=[Tags.GREETING])
def say_hi_body(
        who: str = Body(embed=True),
        other: str = Body(embed=True, default="others")
) -> str:
    """
    query variable url
    use embed for request body processing as simple json
    """
    return f"Hello {who} and {other}"


@router.post("/header", tags=[Tags.GREETING])
def say_hi_headers(who: str = Header()) -> str:
    """Headers variable url"""
    return f"Hello {who}"


class GreetingBody(BaseModel):
    """Model of greeting"""
    greeting_type: str
    address_target: str


@router.get("/better_body")
def say_greeting_to_address(greeting_type: str = "Hello", address_target: str = "world") -> GreetingBody:
    """return model of greeting for given params"""
    return GreetingBody(greeting_type=greeting_type, address_target=address_target)


@router.post("/get_and_return_body")
def get_greeting(greeting_body: GreetingBody) -> GreetingBody:
    """return model of greeting for given params"""
    return GreetingBody(**greeting_body.model_dump())
