from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class MovieRequest(BaseModel):
    title: str

class MovieResponse(BaseModel):
    recommended: List[str]

@router.post("/", response_model=MovieResponse)
def recommend_movies(req: MovieRequest):
    title = req.title.lower()
    dummy_db = {
        "inception": ["Interstellar", "Tenet", "The Prestige"],
        "matrix": ["Inception", "Blade Runner", "Ghost in the Shell"]
    }
    suggestions = dummy_db.get(title, ["No suggestions found."])
    return {"recommended": suggestions}
