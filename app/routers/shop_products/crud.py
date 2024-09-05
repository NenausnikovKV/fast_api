"""CRUD db operations"""
from sqlalchemy.orm import Session

from app.routers.shop_products import models, schemas


def create_shop(db: Session, shop: schemas.CreateShop):
    """create user in database"""
    db_shop = models.Shop(name=shop.name)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop


def get_shop(db: Session, shop_id: int):
    """get shop from db by id"""
    return db.query(models.Shop).filter(models.Shop.id == shop_id).first()


def get_shop_by_name(db: Session, shop_name: str):
    """get shop from db by name"""
    return db.query(models.Shop).filter(models.Shop.name == shop_name).first()


def get_shops(db: Session, skip: int = 0, limit: int = 100):
    """get users from db"""
    return db.query(models.Shop).offset(skip).limit(limit).all()


def create_shop_product(db: Session, product: schemas.ProductCreate, shop_id: int):
    """create product from db dor given user id"""
    db_product = models.Product(**product.model_dump(), shop_id=shop_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    """get products from db"""
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


def get_product(db: Session, product_id: int):
    """get shop from db by id"""
    return db.query(models.Product).filter(models.Product.id == product_id).first()
