class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name = "Mittins", type = "cat", tricks = "jump", health=0, energy=0)

    def walk(self):
        Pet.play(self)
        return self

    def feed(self):
        Pet.eat(self)
        return self

    def bathe(self):
        Pet.noise(self)
        return self 

class Pet(Ninja):
    health = 0
    energy = 0
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self 

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self 

    def noise(self):
        print("Meow")
        return self 

    def display_pet_health_energy(self):
        print(self.name +" Health: " + str(self.health) + " Energy: " + str(self.energy))
        return self

jake = Ninja("Jake", "Miller", "fish", "canned tuna")
mike = Ninja("Mike", "Miller", "fish sticks", "mouse")
mike.pet = Pet("Spot", "Cat", "run", health = 0, energy = 0)


jake.pet.feed().walk().bathe().display_pet_health_energy()
mike.pet.feed().walk().bathe().display_pet_health_energy()




