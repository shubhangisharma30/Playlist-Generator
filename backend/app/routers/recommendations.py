"""
Recommendation router endpoints
"""
from fastapi import APIRouter, Query
from app.schemas.recommendation import RecommendationRequest, RecommendationResponse
from app.services.recommendation_service import RecommendationService

router = APIRouter()
recommendation_service = RecommendationService()


@router.post("/", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """Get song recommendations based on category"""
    return recommendation_service.get_recommendations(request)


@router.get("/", response_model=RecommendationResponse)
async def get_recommendations_get(
    category: str = Query(None, description="Category name (e.g., pop, sad, artist name)"),
    limit: int = Query(5, description="Number of recommendations", ge=1, le=20)
):
    """Get song recommendations based on category (GET endpoint)"""
    request = RecommendationRequest(category=category, limit=limit)
    return recommendation_service.get_recommendations(request)

