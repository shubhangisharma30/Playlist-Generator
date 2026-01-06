"""
Playlist router endpoints
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.playlist import PlaylistCreate, PlaylistResponse, PlaylistUpdate
from app.services.playlist_service import PlaylistService

router = APIRouter()
playlist_service = PlaylistService()


@router.get("/", response_model=List[PlaylistResponse])
async def get_playlists():
    """Get all playlists"""
    return playlist_service.get_all_playlists()


@router.get("/{playlist_id}", response_model=PlaylistResponse)
async def get_playlist(playlist_id: int):
    """Get a specific playlist by ID"""
    playlist = playlist_service.get_playlist_by_id(playlist_id)
    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playlist with ID {playlist_id} not found",
        )
    return playlist


@router.post("/", response_model=PlaylistResponse, status_code=status.HTTP_201_CREATED)
async def create_playlist(playlist: PlaylistCreate):
    """Create a new playlist"""
    return playlist_service.create_playlist(playlist)


@router.put("/{playlist_id}", response_model=PlaylistResponse)
async def update_playlist(playlist_id: int, playlist: PlaylistUpdate):
    """Update an existing playlist"""
    updated_playlist = playlist_service.update_playlist(playlist_id, playlist)
    if not updated_playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playlist with ID {playlist_id} not found",
        )
    return updated_playlist


@router.delete("/{playlist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_playlist(playlist_id: int):
    """Delete a playlist"""
    success = playlist_service.delete_playlist(playlist_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playlist with ID {playlist_id} not found",
        )
