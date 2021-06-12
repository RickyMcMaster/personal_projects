class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "I heard there were monsters!!!"


villager = NPC("Bob", 100, 12)

print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())


class Mother():
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father():
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    # Colt's answer just has pass - the rest is unnecessary
    # def __init__(self): 
    #     super().__init__()
    pass


alex = Child()

print(alex.eye_color, alex.hair_color, alex.hair_type)
print(Child.mro())

class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __str__(self):
        return "{} car train".format(self.num_cars)

    def __len__(self):
        return self.num_cars

a_train = Train(4)
print(a_train)
print(len(a_train))