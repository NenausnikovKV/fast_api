"""Shop products API"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import engine
from app.dependencies import get_db
from app.routers.shop_products import models, crud
from app.routers.shop_products import schemas
from app.tags import Tags

# create db tables
models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/products",
    tags=[Tags.PRODUCT]
)


@router.post("/shop/", response_model=schemas.Shop)
def create_shop(shop: schemas.CreateShop, db: Session = Depends(get_db)):
    """
    create new shop if given name is new
    else raise 400 exception
    """
    db_shop = crud.get_shop_by_name(db, shop_name=shop.name)
    if db_shop:
        raise HTTPException(status_code=400, detail="Shop name already registered")
    return crud.create_shop(db=db, shop=shop)


@router.get("/shops/", response_model=list[schemas.Shop])
def get_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """get shops by limit"""
    shops = crud.get_shops(db, skip=skip, limit=limit)
    return shops


@router.get("/shop/{shop_id}", response_model=schemas.Shop)
def get_shop(shop_id: int, db: Session = Depends(get_db)):
    """gt user pedantic model data"""
    db_shop = crud.get_shop(db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_shop


@router.post("/shop/{shop_id}/product/", response_model=schemas.Product)
def create_product_for_shop(
        shop_id: int,
        product: schemas.ProductCreate,
        db: Session = Depends(get_db)
):
    """create item for given user"""
    db_product = crud.create_shop_product(db=db, product=product, shop_id=shop_id)
    return db_product


@router.get("/products/", response_model=list[schemas.Product])
def get_products(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    """return all shop products"""
    products = crud.get_products(db, skip, limit)
    return products


@router.get("/{product_id}/", response_model=schemas.Product)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    return product for given id
    otherwise raise exception
    """
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
