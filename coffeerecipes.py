from coffeemaking import *
from coffee import *

#-------Concrete Builders----------#
class LatteCoffeeRecipe(CoffeeMaking):
    coffee: Coffee
    def __init__(self):
        self.coffee = Coffee()
    def addName(self):
        self.coffee.setName('Latte')
    def addEspresso(self):
        self.coffee.setEspresso(3)
    def addSugar(self):
        self.coffee.setSugar(0)
    def addCreamer(self):
        self.coffee.setCreamer(True)
    def addMilk(self):
        self.coffee.setMilk(True)
    def addIce(self):
        self.coffee.setCold(True)
    def getCoffee(self):
        return self.coffee

class FlatWhiteCoffeeRecipe(CoffeeMaking):
    coffee: Coffee
    def __init__(self):
        self.coffee = Coffee()
    def addName(self):
        self.coffee.setName('Flat White')
    def addEspresso(self):
        self.coffee.setEspresso(2)
    def addSugar(self):
        self.coffee.setSugar(0)
    def addCreamer(self):
        self.coffee.setCreamer(False)
    def addMilk(self):
        self.coffee.setMilk(True)
    def addIce(self):
        self.coffee.setCold(False)
    def getCoffee(self):
        return self.coffee