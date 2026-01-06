# Playlist Generator API

A FastAPI-based backend for generating and managing playlists with category segregation and song recommendations.

## Features

- **Playlist Management**: Create, read, update, and delete playlists
- **Category Segregation**: Automatically categorize songs by genre and artist
- **Song Recommendations**: Get recommended songs based on categories (dummy data for now)

## Project Structure

```
Playlist-Generator/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── config.py                  # Application configuration
│   ├── routers/                   # API route handlers
│   │   ├── __init__.py
│   │   ├── playlists.py           # Playlist endpoints
│   │   ├── categories.py           # Category endpoints
│   │   └── recommendations.py     # Recommendation endpoints
│   ├── schemas/                   # Pydantic schemas for request/response
│   │   ├── __init__.py
│   │   ├── playlist.py
│   │   ├── category.py
│   │   └── recommendation.py
│   ├── models/                    # Data models
│   │   ├── __init__.py
│   │   └── playlist.py
│   └── services/                  # Business logic layer
│       ├── __init__.py
│       ├── playlist_service.py
│       ├── category_service.py
│       └── recommendation_service.py
├── requirements.txt               # Python dependencies
├── .env.example                  # Example environment variables
├── .gitignore
├── run.py                        # Server startup script
└── README.md
```

## Setup

### 1. Create a Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend Server

**Option 1: Using the run script (Recommended)**

```bash
python run.py
```

**Option 2: Using uvicorn directly**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000` with auto-reload enabled for development.

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Playlists

- `GET /api/v1/playlists/` - Get all playlists
- `GET /api/v1/playlists/{playlist_id}` - Get a specific playlist
- `POST /api/v1/playlists/` - Create a new playlist
- `PUT /api/v1/playlists/{playlist_id}` - Update a playlist
- `DELETE /api/v1/playlists/{playlist_id}` - Delete a playlist

### Categories

- `GET /api/v1/categories/` - Get all categories (genres and artists)
- `GET /api/v1/categories/{category_name}` - Get songs in a specific category
- `GET /api/v1/categories/genre/{genre}` - Get all songs of a specific genre
- `GET /api/v1/categories/artist/{artist}` - Get all songs by a specific artist

### Recommendations

- `GET /api/v1/recommendations/?category=pop&limit=5` - Get song recommendations (GET)
- `POST /api/v1/recommendations/` - Get song recommendations (POST)

## Usage Examples

### Creating a Playlist with Songs

```bash
POST /api/v1/playlists/
{
  "name": "My Pop Playlist",
  "description": "Collection of pop songs",
  "songs": [
    {
      "title": "Pop Song 1",
      "artist": "Artist A",
      "genre": "pop",
      "duration": 180
    },
    {
      "title": "Sad Song 1",
      "artist": "Artist B",
      "genre": "sad",
      "duration": 200
    }
  ]
}
```

### Getting Categories

```bash
# Get all categories
GET /api/v1/categories/

# Get songs in "pop" category
GET /api/v1/categories/pop

# Get songs by specific artist
GET /api/v1/categories/artist/Artist%20A
```

### Getting Recommendations

```bash
# Get recommendations for pop songs
GET /api/v1/recommendations/?category=pop&limit=5

# Get recommendations for sad songs
POST /api/v1/recommendations/
{
  "category": "sad",
  "limit": 3
}
```

## How It Works

1. **Playlist Creation**: Create playlists with songs. Each song can have a `genre` field (e.g., "pop", "rock", "sad").

2. **Category Segregation**: The app automatically:

   - Groups songs by genre (pop, rock, sad, etc.)
   - Groups songs by artist
   - Creates categories dynamically based on your playlists

3. **Recommendations**: Get song recommendations based on categories. Currently uses dummy/sample data. In production, this would integrate with music APIs or ML models.

## Development Notes

- **Current Implementation**: Uses in-memory storage with dummy data
- **Recommendations**: Currently returns sample/dummy recommendations. Replace with real recommendation logic later.
- **Categories**: Automatically generated from playlist songs based on genre and artist fields

## Future Enhancements

For production, consider:

1. Integrate a database (PostgreSQL, MySQL, etc.)
2. Add authentication and authorization
3. Integrate real music APIs (Spotify, Apple Music, etc.) for recommendations
4. Implement proper error handling and logging
5. Add unit and integration tests
6. Set up CI/CD pipeline
7. Add ML-based recommendation engine

## Technologies

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running FastAPI applications
