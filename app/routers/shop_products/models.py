"""sqlalchemy db models"""

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Shop(Base):
    """User table model"""
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    products = relationship("Product", back_populates="shop")


class Product(Base):
    """Item table model"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    price = Column(Float)
    opinion = Column(String)

    # todo set many to many
    shop_id = Column(Integer, ForeignKey("shops.id"))
    shop = relationship("Shop", back_populates="products")
