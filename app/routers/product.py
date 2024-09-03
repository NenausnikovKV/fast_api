"""Shop products API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.routers.tags import Tags


class Product(BaseModel):
    """Shop product"""
    name: str
    description: str | None = None
    producer: str
    price: float
    opinion: str


router = APIRouter(
    prefix="/products",
    tags=[Tags.PRODUCT]
)


products = {
    1: Product(
        name="altay tea",
        description="black bergamot tea",
        producer="altay superfood",
        price=99.90,
        opinion="very bad"
    ),
    2: Product(
        name="stub",
        producer="stub",
        price=0,
        opinion="normal"
    )
}


@router.get("/")
def get_products() -> list[Product]:
    """return all shop products"""
    return list(products.values())


@router.get("/{product_id}")
def get_product_by_id(product_id: int) -> Product:
    """
    return product for given id
    otherwise raise exception
    """
    try:
        product = products[product_id]
        return product
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="item not found") from exc
