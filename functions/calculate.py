def calculate_water(minutes_shower, emission_per_min):
    return minutes_shower * emission_per_min

def calculate_transport(emissions_map, transport, distance):
    emission_rate = emissions_map[transport] #finds how much kg of co2/mi is emitted by mapping choice of trans to emission using dictionary
    return emission_rate * distance

def calculate_meat(burgers_per_week, emission_per_burger):
    return burgers_per_week/7 * emission_per_burger #makes more sense to do burger/week than burger/day
                                                    #so simply ask for weekly amount then divide by 7
