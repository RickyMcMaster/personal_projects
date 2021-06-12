# Define Bank Account Below:
class BankAccount():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, num):
        self.balance += num

    def withdraw(self, num):
        self.balance -= num


class Chicken():
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1


c1 = Chicken("foul", "Jim")
c2 = Chicken("fouler", "Annie")
c1.lay_egg()
c1.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)
