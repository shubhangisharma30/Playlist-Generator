"""
Main FastAPI application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import playlists, categories, recommendations

app = FastAPI(
    title="Playlist Generator API",
    description="API for generating and managing playlists",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(playlists.router, prefix="/api/v1/playlists", tags=["playlists"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(
    recommendations.router, prefix="/api/v1/recommendations", tags=["recommendations"]
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Playlist Generator API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
