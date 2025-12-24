from pydantic import BaseModel

class MovieRequest(BaseModel):
    title: str
    duration: int
    genre: str
    director: str
