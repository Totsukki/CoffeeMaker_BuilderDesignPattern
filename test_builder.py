import unittest
from barista import *
from coffee import *
from coffeemaking import *
from coffeerecipes import *

class TestBuilder(unittest.TestCase):

  def test_getCoffee_should_return_a_latte_coffee_object(self):
    
  #Arrange
    expectedName="Latte"
    expectedEspresso=3
    expectedSugar=0
    expectedCreamer=True
    expectedMilk=True
    expectedCold=False
  #Act
    b = Barista(LatteCoffeeRecipe())
    b.makeCoffee()
    latte = b.getCoffee()
    
  #Assert
    self.assertEqual(latte.name,expectedName)
    self.assertEqual(latte.espresso,expectedEspresso)
    self.assertEqual(latte.sugar,expectedSugar)
    self.assertEqual(latte.creamer,expectedCreamer)
    self.assertEqual(latte.milk,expectedMilk)
    self.assertEqual(latte.cold,expectedCold)

  def test_getCoffee_should_return_a_flat_white_coffee_object(self):
    
  #Arrange
    expectedName="Flat White"
    expectedEspresso=2
    expectedSugar=0
    expectedCreamer=False
    expectedMilk=True
    expectedCold=False
  #Act
    b = Barista(FlatWhiteCoffeeRecipe())
    b.makeCoffee()
    fw = b.getCoffee()
    
  #Assert
    self.assertEqual(fw.name,expectedName)
    self.assertEqual(fw.espresso,expectedEspresso)
    self.assertEqual(fw.sugar,expectedSugar)
    self.assertEqual(fw.creamer,expectedCreamer)
    self.assertEqual(fw.milk,expectedMilk)
    self.assertEqual(fw.cold,expectedCold)

  def test_getCoffee_should_return_a_black_coffee_object(self):
  #Arrange
    expectedName="Black"
    expectedEspresso=3
    expectedSugar=0
    expectedCreamer=False
    expectedMilk=False
    expectedCold=False
  #Act
    b = Barista(BlackCoffeeRecipe())
    b.makeCoffee()
    black = b.getCoffee()
    
  #Assert
    self.assertEqual(black.name,expectedName)
    self.assertEqual(black.espresso,expectedEspresso)
    self.assertEqual(black.sugar,expectedSugar)
    self.assertEqual(black.creamer,expectedCreamer)
    self.assertEqual(black.milk,expectedMilk)
    self.assertEqual(black.cold,expectedCold)
  def test_getCoffee_should_return_a_flat_white_coffee_object(self):
    
  #Arrange
    expectedName="Flat White"
    expectedEspresso=2
    expectedSugar=0
    expectedCreamer=False
    expectedMilk=True
    expectedCold=False
  #Act
    b = Barista(FlatWhiteCoffeeRecipe())
    b.makeCoffee()
    fw = b.getCoffee()
    
  #Assert
    self.assertEqual(fw.name,expectedName)
    self.assertEqual(fw.espresso,expectedEspresso)
    self.assertEqual(fw.sugar,expectedSugar)
    self.assertEqual(fw.creamer,expectedCreamer)
    self.assertEqual(fw.milk,expectedMilk)
    self.assertEqual(fw.cold,expectedCold)

  def test_setSugar_should_change_sugar_level_of_the_coffee(self):
  #Arrange
    expectedValue = .5
  #Act
    b = Barista(BlackCoffeeRecipe())
    b.makeCoffee()
    black = b.getCoffee() # sugar level = 0
    black.setSugar(.5) # sugar level = 0.5 || 50%
  #Assert
    self.assertEqual(black.sugar,expectedValue)

  def test_setCold_should_change_cold_boolean_value_to_true(self):
  #Arrange
    expectedValue = True
  #Act
    b = Barista(LatteCoffeeRecipe())
    b.makeCoffee()
    latte = b.getCoffee() # cold = False
    latte.setCold(True) # cold = True
    
  #Assert
    self.assertEqual(latte.cold, expectedValue)

  def test_setEspresso_should_change_espresso_value_of_the_coffee(self):
  #Arrange
    expectedValue = 3
  #Act
    b = Barista(FlatWhiteCoffeeRecipe())
    b.makeCoffee()
    fw = b.getCoffee() # espresso = 2
    fw.setEspresso(3) # espresso = 3
    
  #Assert
    self.assertEqual(fw.espresso, expectedValue)
  
if __name__ == '__main__':
  unittest.main()