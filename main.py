import math
import random
import time

lang_dict = {
    "en": {
        "menu": """
        CHOOSE YOUR OPTION:
        1 - Create new person
        2 - Kill person
        3 - Show population
        """,
        "kill": "Who do you want to kill? ",
        "type_name": "Type the person's name: ",
        "no_numbers": "No numbers allowed",
        "type_age": "Type the age: ",
        "only_numbers": "Only numbers allowed",
        "no_person": "No person called {} was found",
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
        "die_message": "{}\n{} has died at the age of {} :(\n\"{}\"",
        "age_msg": "\r\n{} has aged by {} years"
    },
    "pt": {
        "menu": """
        ESCOLHA SUA OPÇÃO:
        1 - Criar nova pessoa
        2 - Matar pessoa
        3 - Exibir população
        """,
        "type_name": "Digite o nome da pessoa: ",
        "no_numbers": "Números não são permitidos",
        "type_age": "Digite a idade: ",
        "only_numbers": "Apenas números são permitidos",
        "no_person": "Nenhuma pessoa chamada {} foi encontrada",
        "kill": "Quem você quer matar? ",
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
        "die_message": "{}\n{} morreu aos {} anos :(\n\"{}\"",
        "age_msg": "\r\n{} envelheceu {} anos"
    }
}
class Person:
    humans = []
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
        self.alive = True
        self.life_expectancy = random.randint(70, 100)
        Person.humans.append(self)
        print(lang_choice["init"].format(name,age))
    def __str__(self):
        return lang_choice["str"].format(self.name, self.age, self.alive)
    def get_older(self, years):
        if self.alive:
            self.age+=years
            print(lang_choice["age_msg"].format(self.name, years))
            if self.age == 60:
                print(lang_choice["grandpa_message"].format(self.name))
            if self.roll_death_dice():
                self.die()
        else:
            print(lang_choice["death_message"].format(self.name))
    def die(self):
        self.alive = False
        print(lang_choice["die_message"].format("*"*10,self.name, self.age, random.choice(lang_choice["death_quotes"])))
    def roll_death_dice(self):
        death_chance = pow(self.age/self.life_expectancy, 8) 
        death_chance = min(death_chance, 0.95) # cap the death chance at 95%
        if random.random() < death_chance:
            return True
        else:
            return False
    def auto_age(self):
        while self.alive:
            time.sleep(5) # ages every 5 seconds
            self.get_older(1) 
class Worker(Person):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        self.job = job
        self.salary = salary
    def __str__(self): # operator overload, overriding the __str__ method of the parent class
        text = super(Worker, self).__str__() + lang_choice["worker_str"].format(self.job, self.salary)
        return text
def findPerson(name):
    for person in Person.humans:
        if person.name == name and person.alive:
            return person 
    return False # if we don't find the person in the loop, we return False, meaning we didn't find them
print("PICK YOUR LANGUAGE / ESCOLHA SEU IDIOMA")
lang = input("English (en) / Português (pt): ").lower() # PT, pT ou Pt -> pt
if lang != "en" and lang != "pt":                       # EN, eN ou En -> en
    print("Invalid option, defaulting to English.")
    lang = "en"
lang_choice = lang_dict[lang] # automatically gets the respective language key in the language *dictionary
while True:
    print(lang_choice["menu"])
    choice = input("> ")
    try:
        choice=int(choice)
    except:
        break # not int
    if choice == 1:
        name=input(lang_choice["type_name"])
        try:
            int(name)
            print(lang_choice["no_numbers"])
            break
        except:
            if not name.isalpha(): # verify if name is alphanumeric (a-Z)
                print(lang_choice["no_numbers"])
                break
        age=input(lang_choice["type_age"])
        try:
            age=int(age)
        except:
            print(lang_choice["only_numbers"])
            break
        Person(name, age)
    elif choice == 2:
        name = input(lang_choice["kill"])
        if not isinstance(name, str):
            exit()
        p = findPerson(name)
        if p:
            p.die()
        else:
            print(lang_choice["no_person"].format(name))
    elif choice == 3:
        for human in Person.humans:
            if human.alive:
                print(human)