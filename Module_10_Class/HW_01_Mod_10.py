class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, change):
        self.weight = change


animal = Animal("Simon", 10)
print(animal.weight)
animal.change_weight(12)
print(animal.weight)
