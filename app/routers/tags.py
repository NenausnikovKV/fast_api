"""tags for router docs"""

from enum import Enum


class Tags(Enum):
    """tags for router docs"""
    GREETING = "hi"
    ROOT = "root"


TAGS_METADATA = [
    {
      "name": Tags.ROOT
    },
    {
        "name": Tags.GREETING,
        "description": "Say hello functions"
    }
]
