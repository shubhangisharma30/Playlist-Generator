"""
Category service - business logic for categorizing songs
"""
from typing import List, Dict, Optional
from app.models.playlist import Song
from app.services.playlist_service import PlaylistService
from app.schemas.category import CategoryResponse


class CategoryService:
    """Service for managing song categories"""
    
    def __init__(self):
        self.playlist_service = PlaylistService()
    
    def get_all_categories(self) -> List[CategoryResponse]:
        """Get all categories (genres and artists) from all playlists"""
        # Collect all songs from all playlists
        all_songs: List[Song] = []
        for playlist in self.playlist_service.get_all_playlists():
            all_songs.extend(playlist.songs)
        
        # Group by genre
        genre_categories: Dict[str, List[Song]] = {}
        for song in all_songs:
            if song.genre:
                genre = song.genre.lower()
                if genre not in genre_categories:
                    genre_categories[genre] = []
                genre_categories[genre].append(song)
        
        # Group by artist
        artist_categories: Dict[str, List[Song]] = {}
        for song in all_songs:
            artist = song.artist.lower()
            if artist not in artist_categories:
                artist_categories[artist] = []
            artist_categories[artist].append(song)
        
        # Build category responses
        categories: List[CategoryResponse] = []
        
        # Add genre categories
        for genre, songs in genre_categories.items():
            categories.append(CategoryResponse(
                name=genre,
                type="genre",
                song_count=len(songs),
                songs=songs
            ))
        
        # Add artist categories
        for artist, songs in artist_categories.items():
            categories.append(CategoryResponse(
                name=artist,
                type="artist",
                song_count=len(songs),
                songs=songs
            ))
        
        return categories
    
    def get_category_by_name(self, category_name: str) -> Optional[CategoryResponse]:
        """Get songs in a specific category (genre or artist)"""
        all_categories = self.get_all_categories()
        category_name_lower = category_name.lower()
        
        for category in all_categories:
            if category.name.lower() == category_name_lower:
                return category
        
        return None
    
    def get_songs_by_genre(self, genre: str) -> List[Song]:
        """Get all songs of a specific genre"""
        all_songs: List[Song] = []
        for playlist in self.playlist_service.get_all_playlists():
            all_songs.extend(playlist.songs)
        
        genre_lower = genre.lower()
        return [song for song in all_songs if song.genre and song.genre.lower() == genre_lower]
    
    def get_songs_by_artist(self, artist: str) -> List[Song]:
        """Get all songs by a specific artist"""
        all_songs: List[Song] = []
        for playlist in self.playlist_service.get_all_playlists():
            all_songs.extend(playlist.songs)
        
        artist_lower = artist.lower()
        return [song for song in all_songs if song.artist.lower() == artist_lower]

