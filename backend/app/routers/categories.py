"""
Category router endpoints
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.category import CategoryResponse, CategoryListResponse
from app.schemas.playlist import SongResponse
from app.services.category_service import CategoryService

router = APIRouter()
category_service = CategoryService()


@router.get("/", response_model=CategoryListResponse)
async def get_all_categories():
    """Get all categories (genres and artists)"""
    categories = category_service.get_all_categories()
    return CategoryListResponse(categories=categories, total=len(categories))


@router.get("/{category_name}", response_model=CategoryResponse)
async def get_category(category_name: str):
    """Get songs in a specific category (genre or artist name)"""
    category = category_service.get_category_by_name(category_name)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category '{category_name}' not found",
        )
    return category


@router.get("/genre/{genre}", response_model=List[SongResponse])
async def get_songs_by_genre(genre: str):
    """Get all songs of a specific genre"""
    songs = category_service.get_songs_by_genre(genre)
    return songs


@router.get("/artist/{artist}", response_model=List[SongResponse])
async def get_songs_by_artist(artist: str):
    """Get all songs by a specific artist"""
    songs = category_service.get_songs_by_artist(artist)
    return songs
