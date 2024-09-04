"""Pedantic model"""

from pydantic import BaseModel


class ItemBase(BaseModel):
    """Item base pedantic model"""
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    """Item model for create method"""


class Item(ItemBase):
    """Item pedantic model for read method"""
    id: int
    owner_id: int

    class Config:
        """tell the Pydantic model to read the data even if it is not a dict """
        from_attributes = True


class UserBase(BaseModel):
    """User base pedantic model"""
    email: str


class UserCreate(UserBase):
    """for create method"""
    password: str


class User(UserBase):
    """User pedantic model for read method"""
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        """tell the Pydantic model to read the data even if it is not a dict """
        from_attributes = True
