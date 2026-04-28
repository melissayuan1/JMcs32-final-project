# import from functions folder
from functions.dataload import load_data
from functions.inputs import get_valid_input, get_float
from functions.recs import get_recommendations
from functions.calculate import calculate_transport,calculate_water,calculate_meat

#intial print statement -- tells user their carbon footprint will be calced
print("##CARBON FOOTPRINT CALCULATOR BASED ON TRANSPORTATION, MEAT CONSUMPTION, AND WATER USAGE##")

# Load data -- creates a dictionary
transport_data = load_data('transport.csv', 'transportation', 'emissions')

# user inputs - trans
transport = get_valid_input("Mode of transportation: ", transport_data.keys())
distance = get_float("Miles per day: ")

#calc - transport emissions
transport_emissions = calculate_transport(transport_data, transport, distance)
print(f'Transportation emissions: {transport_emissions:.2f} kg per day')

#user input - shower
shower_time = get_float("Minutes per shower: ")
water_emissions = calculate_water(shower_time, 0.2)
print(f'Shower emissions: {water_emissions:.2f} kg per day')

#use input - meat consumption
burgers_per_week = get_float("Burgers consumed per week: ")
meat_emissions = calculate_meat(burgers_per_week, 2.35)
print(f'Red meat emissions: {meat_emissions:.2f} kg per day')

total = transport_emissions + water_emissions + meat_emissions

# output
print(f"\nTotal Daily CO₂: {total:.2f} kg per day")

# recs
inputs = {"transport": transport, "shower_time": shower_time, "meat_emissions": meat_emissions} #dictionary of category and user results
recs = get_recommendations(inputs) #gets recs using these inputs

#prints suggestions as a list
print("\nSuggestions:")
for r in recs:
    print("-", r)
