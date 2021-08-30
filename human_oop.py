class HumanBeing():
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def __repr__(self):
        return f"{self.name}"

    def walk (self,action):
        print (f"One step {action}")

    def perform (self):
        self.walk("twice")

# Inheritance
class Boy(HumanBeing):
    pass
    # def __repr__(self):
    #     return f"{self.name}"

def main():
    person = HumanBeing("Nana","blackie")
    print(person)
    person.walk("backward")
    person.perform()
    person2 = Boy("Adrian", "White")
    print(person2)
    person2.walk("forward")
    print (isinstance(person2, HumanBeing))


if __name__ == "__main__":
    print("About to run the code \n")
    main()
