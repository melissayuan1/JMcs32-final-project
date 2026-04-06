#The step we are tackling for this assignment is the taking the input of a mode of transportation
#(car, walking, bking etc.) and then a distance travelled, and finding the kg of CO2 produced

# List of valid options

transportation = ['car', 'bike', 'walk', 'train']

# Let user input their data
while True:
    my_transportation = input('What is your usual form of daily transportation?').lower()

    if my_transportation in transportation:
        break
    else:
        print('Accepted modes of transport are: car, bike, walk, train. Try again...')

# Let user input their mileage




