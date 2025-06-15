from fastapi import FastAPI
from app.routes.recommend import router as recommend_router
from app.routes.movies import router as movies_router

app = FastAPI(
    title="Smart Movie Recommender",
    version="1.0.0",
    description="An API that recommends similar movies using content-based filtering"
)

app.include_router(recommend_router, prefix="/api/recommend")
app.include_router(movies_router, prefix="/api/movies")
