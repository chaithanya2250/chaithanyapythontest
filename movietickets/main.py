from fastapi import FastAPI
from schemas import MovieSchema, TheaterSchema, TicketRequest
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



app = FastAPI()

movies = []
theaters = []
tickets = []


@app.get("/movies", response_model=list[MovieSchema])
def get_movies():
    return movies


@app.get("/theater", response_model=TheaterSchema)
def get_theater():
    return TheaterSchema(
        theater_id=1,
        name="Cinema City",
        city="New York"
    )


@app.post("/add_movie", response_model=MovieSchema)
def create_movie(movie_req: MovieSchema):
    movies.append(movie_req)
    return movie_req


@app.post("/book_ticket", response_model=TicketRequest)
def create_ticket(ticket_req: TicketRequest):
    tickets.append(ticket_req)
    return ticket_req

