"""tags for router docs"""

from enum import Enum


class Tags(Enum):
    """tags for router docs"""
    GREETING = "hi"
    ROOT = "root"
    PRODUCT = "product"


TAGS_METADATA = [
    {
      "name": Tags.ROOT
    },
    {
        "name": Tags.GREETING,
        "description": "Say hello functions"
    },
    {
        "name": Tags.PRODUCT,
        "description": "Shop product"
    }
]
