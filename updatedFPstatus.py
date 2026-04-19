# main.py
from modules.dataload import load_data
from modules.inputs import get_valid_input, get_float
from modules.recs import get_recommendations
from modules.calculate import calculate_transport
from modules.calculate import calculate_water

#intial print statement
print("##CARBON FOOTPRINT CALCULATOR BASED ON TRANSPORTATION, ENERGY TYPE, AND WATER USAGE##")

# Load data
transport_data = load_data('data/transport.csv', 'transportation', 'emissions')
energy_data = load_data('data/energytype.csv', 'energy_source', 'emissions')


# user inputs
transport = get_valid_input("Mode of transportation: ", transport_data.keys())
distance = get_float("Miles per day: ")
transport_emissions = calculate_transport(transport_data, transport, distance)
print(f'Transportation emissions: {transport_emissions} kg per day')


energy = get_valid_input("Energy type used: ", energy_data.keys())
shower_time = get_float("Minutes per shower: ")

# calc

water_emissions = calculate_water(shower_time, 0.2)

total = transport_emissions + water_emissions

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
