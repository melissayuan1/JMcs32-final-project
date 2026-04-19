# main.py
from modules.dataload import load_data
from modules.inputs import get_valid_input, get_float
from modules.recs import get_recommendations
from modules.calculate import calculate_transport,calculate_water,calculate_meat

#intial print statement
print("##CARBON FOOTPRINT CALCULATOR BASED ON TRANSPORTATION, MEAT CONSUMPTION, AND WATER USAGE##")

# Load data
transport_data = load_data('data/transport.csv', 'transportation', 'emissions')
energy_data = load_data('data/energytype.csv', 'energy_source', 'emissions')

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
print(f"\nTotal Daily CO₂: {total:.2f} kg")

# recs
inputs = {
    "transport": transport,
    "shower_time": shower_time,
}

recs = get_recommendations(inputs)

print("\nSuggestions:")
for r in recs:
    print("-", r)
