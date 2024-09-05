"""Pedantic model for products section"""
from pydantic import BaseModel


class BaseProduct(BaseModel):
    """Shop product"""
    name: str
    description: str | None = None
    price: float
    opinion: str

    class Config:
        """tell the Pydantic model to read the data even if it is not a dict """
        from_attributes = True


class ProductCreate(BaseProduct):
    """pedantic model for create sqlalchemy model"""


class Product(BaseProduct):
    """API product"""
    id: int
    shop_id: int



class BaseShop(BaseModel):
    """Shop pedantic model"""
    name: str
    products: list[Product] = []

    class Config:
        """tell the Pydantic model to read the data even if it is not a dict """
        from_attributes = True


class CreateShop(BaseShop):
    """create model"""


class Shop(BaseShop):
    """Api shop"""
    id: int
