from fastapi import APIRouter, Query

router = APIRouter()

fake_movie_db = [
    {"id": 1, "title": "The Matrix"},
    {"id": 2, "title": "Inception"},
    {"id": 3, "title": "The Godfather"},
    {"id": 4, "title": "The Matrix Reloaded"}
]

@router.get("/search")
def search_movies(title: str = Query(..., min_length=2)):
    results = [movie for movie in fake_movie_db if title.lower() in movie["title"].lower()]
    return {"results": results}

@router.get("/{movie_id}")
def get_movie_details(movie_id: int):
    for movie in fake_movie_db:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Movie not found"}

@router.post("/rate")
def rate_movie(movie_id: int, rating: float):
    if rating < 0 or rating > 10:
        return {"error": "Rating must be between 0 and 10"}
    return {"message": f"Rating {rating} received for movie ID {movie_id}"}
