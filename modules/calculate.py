def calculate_water(minutes_shower, emission_per_min):
    return minutes_shower * emission_per_min

def calculate_transport(emissions_map, transport, distance):
    emission_rate = emissions_map[transport]
    return emission_rate * distance
