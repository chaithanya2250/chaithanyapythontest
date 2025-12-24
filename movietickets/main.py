import uvicorn
from modals.schemas import MovieSchema, TheaterSchema, TicketRequest, TicketResponse
from fastapi import FastAPI, HTTPException


movies = []  # In-memory storage
theaters = []  # In-memory storage
bookings = []  # In-memory storage
tickets = []  # In-memory storage

app = FastAPI()
@app.get("/movies")
def get_movie():
    return movies   
 
@app.get("/theater")
def get_theater():
    th = TheaterSchema("Cinema City", "New York", 150)
    return TheaterSchema(
        theater_id=th.theater_id,
        name=th.name,
        city=th.city
    )


@app.post("/add_movie")
def create_movie(movie_req: MovieSchema) -> MovieSchema:
    movies.append(movie_req)
    return movie_req

@app.post("/book_ticket", response_model= TicketResponse)
def create_ticket(ticket_req: TicketRequest):
    if is_seat_booked(
        seat_number=ticket_req.seat_number,
        theater_id=ticket_req.theater.theater_id,
        date=ticket_req.date,
        time=ticket_req.time
    ):
      raise HTTPException(
            status_code=400,
            detail=f"Seat {ticket_req.seat_number} is already booked"
        )

    tickets.append(ticket_req)
    return {
        "message": "Ticket booked successfully",
        "ticket": ticket_req
    } 

def is_seat_booked(seat_number: str, theater_id: int, date: str, time: str):
    for ticket in tickets:
        if (ticket.theater.theater_id == theater_id and
            ticket.seat_number == seat_number and
            ticket.date == date and
            ticket.time == time):
            return True
    return False

@app.get("/tickets")
def get_tickets():
   return tickets


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



