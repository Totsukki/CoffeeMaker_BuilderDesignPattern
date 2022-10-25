from barista import *
from coffee import *
from coffeerecipes import *

flatWhiteCoffeeRecipe:CoffeeMaking = FlatWhiteCoffeeRecipe()
latteCoffeeRecipe:CoffeeMaking = LatteCoffeeRecipe()

barista: Barista = Barista(FlatWhiteCoffeeRecipe())
barista.makeCoffee()
print(barista.getCoffee())
# coffee:Coffee = barista.getCoffee()
# print(coffee.toString())

# barista = Barista(latteCoffeeRecipe)
# barista.makeCoffee()
# coffee = barista.getCoffee()
# print('\n' + coffee.toString())
