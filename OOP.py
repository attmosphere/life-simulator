class Person:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
        self.alive = True
        print("Person named {}, age {} got created!".format(name,age))
    def __str__(self):
        return "Name: {}\nAge: {}\nAlive: {}".format(self.name, self.age, self.alive)
    def get_older(self, years):
        if self.alive == True:
            self.age+=years
            if self.age > 90:
                self.die()
        else:
            print("Operation unsuccessful, {} is dead :(".format(self.name))
    def die(self):
        self.alive = False

person1 = Person("Bob",21)
person1.get_older(15)
print(person1)
