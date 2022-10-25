from abc import ABC, abstractmethod

#Abstract Methods
class CoffeeConfig(ABC):
    @abstractmethod
    def setName(self, name:str):
        pass
    @abstractmethod
    def setEspresso(self, espresso:int):
        pass
    @abstractmethod
    def setSugar(self,sugar:int):
        pass
    @abstractmethod
    def setCreamer(self, creamer:bool):
        pass
    def setMilk(self, milk:bool):
        pass
    @abstractmethod
    def setCold(self, cold:bool):
        pass
    
    def toString(self):
        pass
    
class CoffeeMaker(ABC):
    @abstractmethod
    def addName(self):
        pass
    @abstractmethod
    def addEspresso(self):
        pass
    @abstractmethod
    def addSugar(self):
        pass
    @abstractmethod
    def addCreamer(self):
        pass
    def addMilk(self):
        pass
    @abstractmethod
    def addIce(self):
        pass
    @abstractmethod
    def getCoffee(self):
        pass
#--------------------------------------#    

class Coffee(CoffeeConfig):
    name: str
    espresso:int
    sugar:int
    creamer:bool
    milk: bool
    cold:bool
    
    def setName(self, name: str):
        self.name = name
    def setEspresso(self, espresso: int):
        self.espresso = espresso
    def setSugar(self, sugar: int):
        self.sugar = sugar
    def setCreamer(self, creamer:bool):
        self.creamer = creamer
    def setMilk(self, milk: bool):
        self.milk = milk
    def setCold(self, cold:bool):
        self.cold = cold
    def toString(self):
        return f"Order Details: \nName: {self.name}\nEspresso Value (oz.): {self.espresso}\nSugar Value(oz.): {self.sugar}\nCreamer: {self.creamer}\nMilk: {self.milk}\nIced? {self.cold}"
    
class LatteCoffeeMaker(CoffeeMaker):
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

class FlatWhiteCoffeeMaker(CoffeeMaker):
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
    
class Barista:
    coffeeMaker: CoffeeMaker
    def __init__(self, coffeeMaker:CoffeeMaker):
        self.coffeeMaker = coffeeMaker
    def getCoffee(self):
        return self.coffeeMaker.getCoffee()
    def makeCoffee(self):
        self.coffeeMaker.addName()
        self.coffeeMaker.addEspresso()
        self.coffeeMaker.addSugar()
        self.coffeeMaker.addCreamer()
        self.coffeeMaker.addMilk()
        self.coffeeMaker.addIce()
        

    


    