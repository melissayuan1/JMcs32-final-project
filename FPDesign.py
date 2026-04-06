#The step we are tackling for this assignment is the taking the input of a mode of transportation
#(car, walking, bking etc.) and then a distance travelled, and finding the kg of CO2 produced

# List of valid options

transportation = ['car', 'bike', 'walk', 'train', 'plane']

# Let user input their data
my_transportation = input('How did you travel today').lower()

if my_transportation in transportation:
    break
else:
    print('Shape must be rock, paper, or scissors. Try again...')



