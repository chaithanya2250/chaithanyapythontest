from modals import Movie, Theater
from enum import Enum
from datetime import datetime
class Ticket:
    def __init__(self, movie, theater, seat_number, seat_type, price, date, time):
        self.movie = movie
        self.theater = theater
        self.seat_number = seat_number
        self.seat_type = seat_type
        self.price = price
        self.date = date
        self.time = time
