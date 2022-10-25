#-------Product---------#
class Coffee():
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
    
