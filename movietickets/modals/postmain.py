import uvicorn
from fastapi import FastAPI
from modals import Movie
from schemas import MovieRequest

app = FastAPI(title="Movie API")

movies = []  # In-memory storage


@app.post("/movies")
def create_movie(movie_req: MovieRequest):
    movie = Movie(
        title=movie_req.title,
        duration=movie_req.duration,
        genre=movie_req.genre,
        director=movie_req.director
    )
    movies.append(movie)

    return {
        "message": "Movie created successfully",
        "movie": {
            "title": movie.title,
            "duration": movie.duration,
            "genre": movie.genre,
            "director": movie.director
        }
    }
