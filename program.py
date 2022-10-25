from builder import *

flatWhiteCoffeeRecipe:CoffeeRecipe = FlatWhiteCoffeeRecipe()
latteCoffeeRecipe:CoffeeRecipe = LatteCoffeeRecipe()

barista: Barista = Barista(flatWhiteCoffeeRecipe)
barista.makeCoffee()
coffee:Coffee = barista.getCoffee()
print(coffee.toString())

barista = Barista(latteCoffeeRecipe)
barista.makeCoffee()
coffee = barista.getCoffee()
print('\n' + coffee.toString())
