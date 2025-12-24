from pydantic import BaseModel
 
    
class MovieSchema(BaseModel):
    title: str
    duration: int
    genre: str
    director: str


class TheaterSchema(BaseModel):
    theater_id: int
    name: str
    city: str


class TicketRequest(BaseModel):
    movie: MovieSchema
    theater: TheaterSchema
    seat_number: str
    seat_type: str
    price: float
    date: str
    time: str

class TicketResponse(BaseModel):
    message: str
    ticket: TicketRequest
