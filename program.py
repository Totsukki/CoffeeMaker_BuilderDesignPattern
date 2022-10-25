from builder import *

flatWhiteCoffeeMaker:CoffeeMaker = FlatWhiteCoffeeMaker()
barista: Barista = Barista(flatWhiteCoffeeMaker)

barista.makeCoffee()
coffee:Coffee = barista.getCoffee()

print(coffee.toString())