"""
Recommendation service - business logic for song recommendations
"""

from typing import List
from app.models.playlist import Song
from app.services.category_service import CategoryService
from app.schemas.recommendation import RecommendationRequest, RecommendationResponse


class RecommendationService:
    """Service for generating song recommendations"""

    def __init__(self):
        self.category_service = CategoryService()
        # Dummy recommendation database (in real app, this would be from external API or ML model)
        self._dummy_recommendations: dict = {
            "pop": [
                Song(
                    id=1001,
                    title="Popular Pop Hit",
                    artist="Pop Star",
                    genre="pop",
                    duration=195,
                ),
                Song(
                    id=1002,
                    title="Catchy Tune",
                    artist="Top Artist",
                    genre="pop",
                    duration=210,
                ),
                Song(
                    id=1003,
                    title="Summer Vibes",
                    artist="Chart Topper",
                    genre="pop",
                    duration=185,
                ),
            ],
            "sad": [
                Song(
                    id=2001,
                    title="Emotional Ballad",
                    artist="Soul Singer",
                    genre="sad",
                    duration=240,
                ),
                Song(
                    id=2002,
                    title="Melancholy Melody",
                    artist="Heartfelt Artist",
                    genre="sad",
                    duration=220,
                ),
                Song(
                    id=2003,
                    title="Tears and Rain",
                    artist="Emotional Voice",
                    genre="sad",
                    duration=260,
                ),
            ],
            "rock": [
                Song(
                    id=3001,
                    title="Rock Anthem",
                    artist="Rock Band",
                    genre="rock",
                    duration=280,
                ),
                Song(
                    id=3002,
                    title="Electric Guitar",
                    artist="Hard Rockers",
                    genre="rock",
                    duration=250,
                ),
                Song(
                    id=3003,
                    title="Power Chord",
                    artist="Rock Legends",
                    genre="rock",
                    duration=270,
                ),
            ],
        }

    def get_recommendations(
        self, request: RecommendationRequest
    ) -> RecommendationResponse:
        """Get song recommendations based on category"""
        category = request.category.lower() if request.category else None
        limit = request.limit or 5

        if not category:
            # Return random recommendations if no category specified
            recommended_songs = self._get_random_recommendations(limit)
            category = "general"
        else:
            # Get recommendations for specific category
            recommended_songs = self._get_category_recommendations(category, limit)

        return RecommendationResponse(
            category=category,
            recommended_songs=recommended_songs,
            count=len(recommended_songs),
        )

    def _get_category_recommendations(self, category: str, limit: int) -> List[Song]:
        """Get recommendations for a specific category"""
        # Check if we have dummy recommendations for this category
        if category in self._dummy_recommendations:
            return self._dummy_recommendations[category][:limit]

        # If category exists in playlists, return some dummy recommendations
        category_data = self.category_service.get_category_by_name(category)
        if category_data:
            # Return dummy recommendations based on category type
            if category_data.type == "genre":
                # Return genre-based recommendations
                genre_recs = self._dummy_recommendations.get(category, [])
                if not genre_recs:
                    # Fallback: create generic recommendations
                    genre_recs = [
                        Song(
                            id=9999,
                            title=f"Recommended {category.title()} Song",
                            artist="Recommended Artist",
                            genre=category,
                            duration=200,
                        )
                    ]
                return genre_recs[:limit]
            else:
                # Artist-based: recommend similar artists (dummy)
                return [
                    Song(
                        id=8888,
                        title=f"Similar to {category.title()}",
                        artist="Similar Artist",
                        genre="pop",
                        duration=190,
                    )
                ][:limit]

        # Default: return generic recommendations
        return self._get_random_recommendations(limit)

    def _get_random_recommendations(self, limit: int) -> List[Song]:
        """Get random recommendations"""
        all_recs = []
        for recs in self._dummy_recommendations.values():
            all_recs.extend(recs)
        return all_recs[:limit]
