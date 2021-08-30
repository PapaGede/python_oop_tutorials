class Vehicle:
# default constructor 
    def __init__(self, name, max_speed, mileage, capacity, color = "white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.capacity = capacity

# serves as the output message anytime the __init__ method is called
    def __repr__(self):
        return f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


# a method with a different parameter for finding the seating capacity of the vehicle
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare (self):
        return self.capacity * 100


class Bus (Vehicle):
# overriding the seating_capacity method by setting a default number
    def seating_capacity (self, capacity = 50):
        return super().seating_capacity(capacity)
        # Super is the class currently in

# overriding the fare method by adding 10& to the main fare
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return f"Total fare is {amount}"


# class DoubleDecker (Bus):
#     def seating_capacity (self, capacity = 100):
#         return super().super


# A new instance of the vehicle class
corolla = Vehicle("Corolla", "180", "12", 45)

print (corolla, "\n")

# Created an instance of the child class
trotro = Bus("Audi Q5", "240", "18", 50)

print (trotro , "\n")

print(trotro.seating_capacity() , "\n")

print (trotro.fare())