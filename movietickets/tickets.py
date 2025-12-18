class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code    

        

class hall(Theater):
    def __init__(self, name, city, seating_capacity, hall_number):
        super().__init__(name, city, seating_capacity)
        self.hall_number = hall_number

class showtime:
    def __init__(self, name,showtime):
        self.name = name
        self.showtime = showtime

    

class customer:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    
class payment:
    def __init__(self, payment_method):
         #make for loop to calaculate total amount for multiple tickets
        self.tickets: list[ticket] = []
        self.payment_method = payment_method
        self.price = 0.0

    def process_payment(self, list_of_tickets):
        total_amount = sum(ticket.price for ticket in list_of_tickets)
        self.price = total_amount        
        print(f"Processing payment of ${self.price} via {self.payment_method}")

    def refund_payment(self):
        print(f"Refunding payment of ${self.price} via {self.payment_method}")  

    def generate_receipt(self):
        print("Generating receipt...")
        print(f"Ticket Number: {self.ticket_number}, Seat Number: {self.seat_number}, Price: ${self.price}, Payment Method: {self.payment_method}")        

class booking:
    def __init__(self, customer: customer, tickets):
        self.customer = customer
        self.tickets : list[ticket] = []
        self.booking_date = datetime.now()        

    def confirm_booking(self):
        print(f"Booking confirmed for {self.customer.name} on {self.booking_date}")
        for ticket in self.tickets:
            ticket.display_ticket_info()

    def cancel_booking(self):
        print(f"Booking cancelled for {self.customer.name} on {self.booking_date}")
        for ticket in self.tickets:
            ticket.display_ticket_info()


class notifications:
    def __init__(self, notification_method):
        self.notification_method = notification_method

    def send_booking_confirmation(self):
        print(f"Sending booking confirmation via {self.notification_method}")

    def send_cancellation_confirmation(self):
        print(f"Sending cancellation confirmation via {self.notification_method}")

    def send_reminder(self):
        print(f"Sending reminder via {self.notification_method}")   





        
