from abc import ABC, abstractmethod

#Abstract Classes
from coffeemaking import *

#------Director-------#
class Barista:
    coffeeMaking: CoffeeMaking
    def __init__(self, coffeeMaking: CoffeeMaking):
        self.coffeeMaking= coffeeMaking
    def getCoffee(self):
        return self.coffeeMaking.getCoffee()
    def makeCoffee(self):
        self.coffeeMaking.addName()
        self.coffeeMaking.addEspresso()
        self.coffeeMaking.addSugar()
        self.coffeeMaking.addCreamer()
        self.coffeeMaking.addMilk()
        self.coffeeMaking.addIce()
        

    


    