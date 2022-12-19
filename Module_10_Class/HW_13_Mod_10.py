class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog(Cat):
    def say(self):
        return "Woof"


tuzik = CatDog('Tuzik', 33)
print(tuzik.say())