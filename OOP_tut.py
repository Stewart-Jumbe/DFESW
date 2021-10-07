from abc import ABC, abstractmethod
import randint from random

class Bird(ABC): #Superclass
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):# first subclass, used inheretance to create this child class

    def reproduce(self):
        self.babies += 6 #used Polymorphism to override the reproduce method

    def eat(self):# used Abstraction with eat method
        return "Peck peck"
    
class Dodo(Bird):
    Fly = False # Used Polymorphism to override the fly and reproduce method 
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):# Encapsulation used to keep the babies variable from being directly accessed as well as inheritance to create a child class of bird
        if not self.extinct:
            self.babies += 1

class Dragon(Bird):
    Fly = True
    extinct = 'Unknown'

    def eat(self):
        return
#creating objects
liam = Dodo()
bruce = Owl()
print(liam.eat())
print(bruce.fly)
