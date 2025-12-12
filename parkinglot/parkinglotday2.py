class parking_lot:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

class parking_floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number        

class parking_spot:
    def __init__(self, spot_number, vehicle_type):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type

class smallvechicle(parking_spot):
    def __init__(self, spot_number, vehicle_type):
        super().__init__(spot_number, vehicle_type)   

class largevechicle(parking_spot):
    def __init__(self, spot_number, vehicle_type):
        super().__init__(spot_number, vehicle_type)

class electricvechicle(parking_spot):
    def __init__(self, spot_number, vehicle_type):
        super().__init__(spot_number, vehicle_type)

class handicaped(parking_spot):
    def __init__(self, spot_number, vehicle_type):
        super().__init__(spot_number, vehicle_type)

class xlvechicle(parking_spot):
    def __init__(self, spot_number, vehicle_type):
        super().__init__(spot_number, vehicle_type)       


class vechicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class car(vechicle):
    def __init__(self):
        super().__init__()

class specialvechicle(vechicle):
    def __init__(self):
        super().__init__()

class   truckvechicle(vechicle):
    def __init__(self):
        super().__init__()

class motorcycle(vechicle):
    def __init__(self):
        super().__init__()  

class electricvechicle(vechicle):
    def __init__(self):
        super().__init__()


class user:
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password

class admin(user):
    def __init__(self, username, name, password):
        super().__init__(username, name, password)

class attendant(user):
    def __init__(self, username, name, password):
        super().__init__(username, name, password)

                       
