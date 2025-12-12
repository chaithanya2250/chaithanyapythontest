
class vechicle:
    def __init__(self):
        pass
    
class car(vechicle):
    def __init__(self):
        super().__init__()

class motorcycle(vechicle):
    def __init__(self):
        super().__init__()

class truck(vechicle):
    def __init__(self):
        super().__init__()

class speicalvechicle(vechicle):
    def __init__(self):
        super().__init__()

class electricvechicle(vechicle):
    def __init__(self):
        super().__init__()

park_spots = 30
park_floors = 10
speicalvechicle_spots = 5
electricvechicle_spots = 5  
truck_spots = 10
motorcycle_spots = 6
car_spots = 7
class parkinglot:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

class parking_floor(parkinglot):
    def __init__(self, name, location, capacity, floor_number):
        super().__init__(name, location, capacity)
        self.floor_number = floor_number

class parking_spot(parking_floor):
    def __init__(self, name, location, capacity, floor_number, spot_number, vehicle_type):
        super().__init__(name, location, capacity, floor_number)
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        if vehicle_type == 'car':
            

print("welcome to Johnson parking lot management system")
print("Please select your purpose:")
print("1. Park")
print("2. Unpark")
print("3. Status")
print("4. Exit") 
option = input("Enter option (1-4): ")
if option == '1':
    print("Please select your vechicle type:")
    print("1. Car")
    print("2. Motorcycle")
    print("3. SpecialVechicle")
    print("4. ElectricVechicle")
    print("5. Truck") 
   
    vehicle_type = input("Enter vehicle type (car/bike/truck): ").lower()
    
    if vehicle_type == 'car':
        print("Parking a car...")
    elif vehicle_type == 'motorcycle':
        print("Parking a motorcycle...")
    elif vehicle_type == 'truck':
        print("Parking a truck...")
    elif vehicle_type == 'specialvechicle':
        print("Parking a special vehicle...")
    elif vehicle_type == 'electricvechicle':
        print("Parking an electric vehicle...")            
    else:
        print("Invalid vehicle type.")
