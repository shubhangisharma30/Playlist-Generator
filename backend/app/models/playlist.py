"""
Database models for Playlist (for future database integration)
"""

from datetime import datetime
from typing import List, Optional


class Song:
    """Song model"""

    def __init__(
        self,
        id: int,
        title: str,
        artist: str,
        genre: Optional[str] = None,
        duration: Optional[int] = None,
    ):
        self.id = id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration


class Playlist:
    """Playlist model"""

    def __init__(
        self,
        id: int,
        name: str,
        description: Optional[str] = None,
        songs: Optional[List[Song]] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.songs = songs or []
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
