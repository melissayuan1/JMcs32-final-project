#The step we are tackling for this assignment is the taking the input of a mode of transportation
#(car, walking, bking etc.) and then a distance travelled, and finding the kg of CO2 produced

# List of valid options
# Open file of transportation options
import csv

transportation = []

with open('data1.csv') as file:
    reader = csv.DictReader(file)  # reads rows as dictionaries

    for row in reader:
        transportation.append(row['transportation'])

print(transportation)


# Let user input their data
while True:
    my_transportation = input('Pick your usual form of daily transportation from these option!').lower()

    if my_transportation in transportation:
        break
    else:
        print('Accepted modes of transport are: car, bike, walk, train. Try again...')

# Take inputs of carbon footprints from different modes of transport, match to user input.
per_kilometer = ####

# Let user input their mileage
my_distance = input('How far do you travel on an average day —— think your commute, going to school, and other daily destinations!')

# Calculate total mileage
transportation_footprint = per_kilometer * my_distance


