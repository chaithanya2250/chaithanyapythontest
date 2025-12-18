import uvicorn
from modals.Movie import Movie 
from modals.Theater import Theater
from fastapi import FastAPI

app = FastAPI()
@app.get("/movie")
def get_movie():
    movie_obj = Movie.Movie("The Matrix", 136, "Sci-Fi", "The Wachowskis")
    return [
        {
            "title": movie_obj.title,
            "duration": movie_obj.duration,
            "genre": movie_obj.genre,
            "director": movie_obj.director
        }
    ]

@app.get("/theater")
def get_theater():
    th = Theater("Cinema City", "New York", 150)
    return [
        {
            "name": th.name,
            "city": th.city,
            "seating_capacity": th.seating_capacity
        }
    ]
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



