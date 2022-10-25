from abc import ABC, abstractmethod
#----------Builder-------------#
class CoffeeMaking(ABC):
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