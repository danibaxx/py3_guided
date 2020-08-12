from category import Category
from product import Sneaker
from product import SoccerBall

# create a department store with terminal interface
class Store:
    # attributes - name, categories(departments)

    # constructor (OOP Term) - the function that runs every time you create a new instance
    # self(this in JS) refers to the current instance of the class
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    #__xxx__ == dunder methods
    def __str__(self):
        # return a string representing the store to the user
        output = f'Welcome to {self.name}!'
        i = 1
        for category in self.categories:
            output += f'\n {i}. {category.name}'
            # return f'Welcome to {self.name}: Here are the categories {self.categories}'
            i += 1
        return output

    def __repr__(self):
        # also returns a string which helps devs understand how your object is structured
        return f'self.name = {self.name} ; self.categories = {self.categories}'

nike_free = Sneaker('100', 'Nike Free', '10', 'Nike')
soccer_ball = SoccerBall('Wilson', '20', 'Rubber')

running_category = Category('Running', 'All your running needs', [nike_free])
baseball_category = Category('Baseball', 'Blue Jays Fans only', [])
basketball_category = Category('Basketball', 'Indoor and outdoor products', [])
football_category = Category('Football', 'The American kind', [])
soccer_category = Category('Soccer', 'The real football', [soccer_ball])

sports_store = Store('Gander Mountain', [running_category, baseball_category, basketball_category, football_category, soccer_category])
# grocery_store = Store('Smiths', ('Dairy', 'Meat', 'Produce', 'Grocery'))

# str(sports_store)
# print(sports_store)
# print(grocery_store)
# print(sports_store.name)
# print(repr(sports_store))

choice = -1
# REPL <- Read Evaluate Print Loop
# read
print(sports_store)
print('type q to quit')
# print('Type 0 to quit')
while True:
  choice = input('Please choose a category (#): ')
  try:
    # evaluate
    if (choice == 'q'):
      break
    choice = int(choice) - 1
    if choice >= 0 and choice < len(sports_store.categories):
      chosen_category = sports_store.categories[choice] 
      # print
      print(chosen_category)
    else:
      print('The number is out of range')

  except ValueError:
    print('Please enter a valid number')