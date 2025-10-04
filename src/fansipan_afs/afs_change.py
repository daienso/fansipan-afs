"""
Types of changes
"""
from enum import Enum

class ChangeTypeClassEnum(str, Enum):
    """Type of changes
    """
    UPDATE = "update"
    DELETE = "delete"
    NEW = "new"
    UNAVAILABLE = "unavailable"
