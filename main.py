import math
import random
import time

lang_dict = {
    "en": {
        "death_quotes": ["I have no regrets.",
                        "I wish I had more time.",
                        "I wish I had more time with my loved ones.",
                        "I wish I had more time to do the things I love."],
        "enter_name": "Enter your name: ",
        "enter_age": "Enter your age: ",
        "get_older": "Do you want to get older? (y/n) ",
        "goodbye": "Goodbye {}! :C",
        "create_worker": "Do you want to create a worker? (y/n) ",
        "create_worker_message": "Let's create a worker and see how they age...\n",
        "grandpa_message": "Grandpa/grandma {} is getting old...",
        "confirm_y": "y",
        "confirm_n": "n",
        "init": "Person named {}, age {} got created!",
        "str": "Name: {}\nAge: {}\nAlive: {}",
        "worker_str": "\nJob: {}\nSalary: {}",
        "die_message": "{}\n{} has died at the age of {} :(\n\"{}\""
    },
    "pt": {
        "death_quotes": ["Não tenho arrependimentos.",
                        "Gostaria de ter tido mais tempo.",
                        "Gostaria de ter tido mais tempo com meus entes queridos.",
                        "Gostaria de ter tido mais tempo para fazer as coisas que amo."],
        "enter_name": "Digite seu nome: ",
        "enter_age": "Digite sua idade: ",
        "get_older": "Você quer envelhecer? (s/n) ",
        "goodbye": "Adeus {}! :C",
        "create_worker": "Você quer criar um trabalhador? (s/n) ",
        "create_worker_message": "Vamos criar um trabalhador e ver como ele envelhece...\n",
        "grandpa_message": "Vovô/vovó {} está ficando velho...",
        "confirm_y": "s",
        "confirm_n": "n",
        "init": "Pessoa chamada {}, idade {} foi criada!",
        "str": "Nome: {}\nIdade: {}\nVivo: {}",
        "worker_str": "\nTrabalho: {}\nSalário: {}",
        "die_message": "{}\n{} morreu aos {} anos :(\n\"{}\""
    }
}
class Person:
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
        self.alive = True
        self.life_expectancy = random.randint(70, 100)
        print(lang_choice["init"].format(name,age))
    def __str__(self):
        return lang_choice["str"].format(self.name, self.age, self.alive)
    def get_older(self, years):
        if self.alive:
            self.age+=years
            if self.roll_death_dice():
                self.die()
        else:
            print(lang_choice["death_message"].format(self.name))
    def die(self):
        self.alive = False
        print(lang_choice["die_message"].format("*"*10,self.name, self.age, random.choice(lang_choice["death_quotes"])))
    def roll_death_dice(self):
        death_chance = math.pow(self.age/self.life_expectancy, 8) 
        death_chance = min(death_chance, 0.95) # cap the death chance at 95%
        if random.random() < death_chance:
            return True
        else:
            return False

class Worker(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        self.job = job
        self.salary = salary
    def __str__(self): # overriding the __str__ method of the parent class
        text = super(Worker, self).__str__() + lang_choice["worker_str"].format(self.job, self.salary)
        return text

print("PICK YOUR LANGUAGE / ESCOLHA SEU IDIOMA")
lang = input("English (en) / Português (pt): ").lower()
if lang != "en" and lang != "pt":
    print("Invalid language, defaulting to English.")
    lang = "en"
lang_choice = lang_dict[lang] # automatically gets the respective language key in the language *dictionary
name = str(input(lang_choice["enter_name"]))
age = int(input(lang_choice["enter_age"]))
person1 = Person(name, age)
print(person1)
while input(lang_choice["get_older"]) != "n" and person1.alive: 
    person1.get_older(random.randint(1,3))
    print(person1)
print(lang_choice["goodbye"].format(person1.name))
print("\n\n\n")
time.sleep(1.5)
if input(lang_choice["create_worker"]).lower() == "n": exit()
print(lang_choice["create_worker_message"])
time.sleep(1.5)
worker1 = Worker("Alice", 30, "Software Engineer", 2500) # monthly salary
print(worker1,"\nLife expectancy:",worker1.life_expectancy)
while worker1.alive:
    # print(worker1)
    print("Age: {}".format(worker1.age))
    if worker1.age > 60 and worker1.age <= 67:
        print(lang_choice["grandpa_message"].format(worker1.name))
        time.sleep(1)
    worker1.get_older(random.randint(1,3))
    time.sleep(0.25)
