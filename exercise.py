class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"The {self.color} car has {self.mileage} miles"

def main():
    car1 = Car("blue", "20,000")
    print(car1)
    car2 = Car("red", "30,000")
    print(car2)

if __name__ == "__main__":
    main()
