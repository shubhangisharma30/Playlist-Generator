"""
Playlist service - business logic layer
"""
from typing import List, Optional
from datetime import datetime
from app.models.playlist import Playlist, Song
from app.schemas.playlist import PlaylistCreate, PlaylistUpdate


class PlaylistService:
    """Service for managing playlists"""
    
    def __init__(self):
        # In-memory storage (replace with database in production)
        self._playlists: List[Playlist] = []
        self._next_id = 1
        self._next_song_id = 1
        
        # Initialize with sample data
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with sample playlists"""
        # Sample playlist with songs of different genres
        sample_playlist = Playlist(
            id=self._next_id,
            name="My First Playlist",
            description="A sample playlist with various genres",
            songs=[
                Song(id=self._next_song_id, title="Pop Song 1", artist="Artist A", genre="pop", duration=180),
                Song(id=self._next_song_id + 1, title="Sad Song 1", artist="Artist B", genre="sad", duration=200),
                Song(id=self._next_song_id + 2, title="Rock Song 1", artist="Artist C", genre="rock", duration=220),
                Song(id=self._next_song_id + 3, title="Pop Song 2", artist="Artist A", genre="pop", duration=190),
            ]
        )
        self._next_id += 1
        self._next_song_id += 4
        self._playlists.append(sample_playlist)
    
    def get_all_playlists(self) -> List[Playlist]:
        """Get all playlists"""
        return self._playlists
    
    def get_playlist_by_id(self, playlist_id: int) -> Optional[Playlist]:
        """Get a playlist by ID"""
        return next((p for p in self._playlists if p.id == playlist_id), None)
    
    def create_playlist(self, playlist_data: PlaylistCreate) -> Playlist:
        """Create a new playlist"""
        songs = []
        for song_data in playlist_data.songs:
            song = Song(
                id=self._next_song_id,
                title=song_data.title,
                artist=song_data.artist,
                genre=song_data.genre,
                duration=song_data.duration
            )
            songs.append(song)
            self._next_song_id += 1
        
        playlist = Playlist(
            id=self._next_id,
            name=playlist_data.name,
            description=playlist_data.description,
            songs=songs,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self._next_id += 1
        self._playlists.append(playlist)
        return playlist
    
    def update_playlist(self, playlist_id: int, playlist_data: PlaylistUpdate) -> Optional[Playlist]:
        """Update an existing playlist"""
        playlist = self.get_playlist_by_id(playlist_id)
        if not playlist:
            return None
        
        if playlist_data.name is not None:
            playlist.name = playlist_data.name
        if playlist_data.description is not None:
            playlist.description = playlist_data.description
        if playlist_data.songs is not None:
            songs = []
            for song_data in playlist_data.songs:
                song = Song(
                    id=self._next_song_id,
                    title=song_data.title,
                    artist=song_data.artist,
                    genre=song_data.genre,
                    duration=song_data.duration
                )
                songs.append(song)
                self._next_song_id += 1
            playlist.songs = songs
        
        playlist.updated_at = datetime.now()
        return playlist
    
    def delete_playlist(self, playlist_id: int) -> bool:
        """Delete a playlist"""
        playlist = self.get_playlist_by_id(playlist_id)
        if not playlist:
            return False
        
        self._playlists.remove(playlist)
        return True

