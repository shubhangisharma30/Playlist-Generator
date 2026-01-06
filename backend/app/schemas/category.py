"""
Pydantic schemas for Category models
"""

from pydantic import BaseModel, Field
from typing import List
from app.schemas.playlist import SongResponse


class CategoryResponse(BaseModel):
    """Schema for category response"""

    name: str = Field(..., description="Category name (e.g., pop, rock, artist name)")
    type: str = Field(..., description="Category type: 'genre' or 'artist'")
    song_count: int = Field(..., description="Number of songs in this category")
    songs: List[SongResponse] = Field(
        default_factory=list, description="Songs in this category"
    )

    class Config:
        from_attributes = True


class CategoryListResponse(BaseModel):
    """Schema for list of categories"""

    categories: List[CategoryResponse] = Field(default_factory=list)
    total: int = Field(..., description="Total number of categories")
