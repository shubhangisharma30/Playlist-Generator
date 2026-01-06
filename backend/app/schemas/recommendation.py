"""
Pydantic schemas for Recommendation models
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.playlist import SongResponse


class RecommendationRequest(BaseModel):
    """Schema for recommendation request"""

    category: Optional[str] = Field(
        None, description="Category name (e.g., pop, sad, artist name)"
    )
    limit: Optional[int] = Field(
        5, description="Number of recommendations", ge=1, le=20
    )


class RecommendationResponse(BaseModel):
    """Schema for recommendation response"""

    category: str = Field(
        ..., description="Category for which recommendations are provided"
    )
    recommended_songs: List[SongResponse] = Field(
        default_factory=list, description="Recommended songs"
    )
    count: int = Field(..., description="Number of recommendations")
