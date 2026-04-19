# import from functions folder
from functions.dataload import load_data
from functions.inputs import get_valid_input, get_float
from functions.recs import get_recommendations
from functions.calculate import calculate_transport,calculate_water,calculate_meat

#intial print statement -- tells user their carbon footprint will be calced
print("##CARBON FOOTPRINT CALCULATOR BASED ON TRANSPORTATION, MEAT CONSUMPTION, AND WATER USAGE##")

# Load data -- creates a dictionary
transport_data = load_data('transport.csv', 'transportation', 'emissions')

# TRANSPORTATION:
transport = get_valid_input("\nMode of transportation: ", transport_data.keys()) #.keys() method for retrieving current keys aka valid options
distance = get_float("Miles per day: ") #grabs user dist
transport_emissions = calculate_transport(transport_data, transport, distance) #calculates
print(f'Transportation emissions: {transport_emissions:.2f} kg per day') #outputs

#SHOWER:
shower_time = get_float("\nMinutes per shower: ") #grabs user input
water_emissions = calculate_water(shower_time, 0.2) #grabs user input
print(f'Shower emissions: {water_emissions:.2f} kg per day') #outputs

#MEAT CONSUMP:
burgers_per_week = get_float("\nBurgers consumed per week: ") #grabs user input
meat_emissions = calculate_meat(burgers_per_week, 2.35) #grabs user input
print(f'Red meat emissions: {meat_emissions:.2f} kg per day')  #outputs

#TOTAL CARBON FOOTPRINT
total = transport_emissions + water_emissions + meat_emissions #sums
print(f"\nTotal Daily CO₂: {total:.2f} kg per day") # outputs

# recs
inputs = {"transport": transport, "shower_time": shower_time, "meat_emissions": meat_emissions} #dictionary of category and user results
recs = get_recommendations(inputs) #gets recs using these inputs

#prints suggestions as a list
print("\nSuggestions:")
for r in recs:
    print("-", r)
