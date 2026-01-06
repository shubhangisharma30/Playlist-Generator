"""
Pydantic schemas for Playlist models
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class SongBase(BaseModel):
    """Base song schema"""

    title: str = Field(..., description="Song title")
    artist: str = Field(..., description="Artist name")
    genre: Optional[str] = Field(
        None, description="Song genre/category (e.g., pop, rock, sad)"
    )
    duration: Optional[int] = Field(None, description="Duration in seconds")


class SongCreate(SongBase):
    """Schema for creating a song"""

    pass


class SongResponse(SongBase):
    """Schema for song response"""

    id: int

    class Config:
        from_attributes = True


class PlaylistBase(BaseModel):
    """Base playlist schema"""

    name: str = Field(..., description="Playlist name", min_length=1, max_length=100)
    description: Optional[str] = Field(
        None, description="Playlist description", max_length=500
    )


class PlaylistCreate(PlaylistBase):
    """Schema for creating a playlist"""

    songs: Optional[List[SongCreate]] = Field(
        default_factory=list, description="List of songs"
    )


class PlaylistUpdate(BaseModel):
    """Schema for updating a playlist"""

    name: Optional[str] = Field(
        None, description="Playlist name", min_length=1, max_length=100
    )
    description: Optional[str] = Field(
        None, description="Playlist description", max_length=500
    )
    songs: Optional[List[SongCreate]] = Field(None, description="List of songs")


class PlaylistResponse(PlaylistBase):
    """Schema for playlist response"""

    id: int
    songs: List[SongResponse] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
