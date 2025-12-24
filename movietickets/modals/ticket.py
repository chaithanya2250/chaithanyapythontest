from modals import Movie, Theater
from enum import Enum
from datetime import datetime


class ticket:
    def __init__(self, movie: Movie, theater: Theater, seat_number, seat_type, price, date, time):
        self.movie = movie
        self.theater = theater
        self.seat_number = seat_number
        self.seat_type = seat_type
        self.price = price
        self.date = date
        self.time = time
           

    def display_ticket_info(self):
        print(f"Movie: {self.movie.title}")
        print(f"Theater: {self.theater.name}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: ${self.price}")  
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
       