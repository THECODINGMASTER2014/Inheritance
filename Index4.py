class Vehicle :
    def __init__(self, fareperkm):
        self.fareperkm = fareperkm

class Bus(Vehicle):
    pass

x = int(input("Enter Km : "))
School_Bus = Bus(20)
total_fare = School_Bus.fareperkm * x
print("$",total_fare)