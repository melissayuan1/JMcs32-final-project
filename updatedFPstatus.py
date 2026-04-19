# main.py

from modules.dataload import load_data
from modules.inputs import get_valid_input, get_float
from modules.recs import get_recommendations

# Load data
transport_data = load_data('data/transport.csv', 'transportation', 'emissions')
energy_data = load_data('data/energytype.csv', 'energy_source', 'emissions')

# user inputs
transport = get_valid_input("Transport: ", transport_data.keys())
energy = get_valid_input("Energy: ", energy_data.keys())
distance = get_float("Miles per day: ")
shower_time = get_float("Minutes per shower: ")

# calc
def calculate_water(minutes_shower, emission_per_min):
    return minutes_shower * emission_per_min
def calculate_transport(emissions_map, transport, distance):
    emission_rate = emissions_map[transport]
    return emission_rate * distance

transport_emissions = calculate_transport(transport_data, transport, distance)
#food_emissions = calculate_food(meat, servings, food_data)
water_emissions = calculate_water(shower_time, 0.2)

total = transport_emissions + water_emissions

# --- OUTPUT ---
print(f"\nTotal Daily CO₂: {total:.2f} kg")

# --- RECOMMENDATIONS ---
inputs = {
    "transport": transport,
    "shower_time": shower_time,
}

recs = get_recommendations(inputs)

print("\nSuggestions:")
for r in recs:
    print("-", r)
