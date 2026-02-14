import random
import time

class Person:
    death_quotes = ["I have no regrets.",
                    "I wish I had more time.",
                    "I wish I had more time with my loved ones.",
                    "I wish I had more time to do the things I love."]
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
        print("{} has died at the age of {} :(\n\"{}\"".format(self.name, self.age, random.choice(Person.death_quotes)))
class Worker(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        self.job = job
        self.salary = salary
    def __str__(self): # overriding the __str__ method of the parent class
        text = super(Worker, self).__str__() + "\nJob: {}\nSalary: {}".format(self.job, self.salary)
        return text
    
person1 = Person("Bob", 21)
person1.get_older(15)
print(person1)

worker1 = Worker("Alice", 30, "Software Engineer", 2500) # monthly salary
print(worker1)
while worker1.alive:
    worker1.get_older(random.randint(1,10))
    time.sleep(2)
    print(worker1)
