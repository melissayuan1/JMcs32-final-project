def get_recommendations(inputs):
    recs = [] #empty list of recs
    #any option other than public transit, walking, and biking will recieve this rec
    if inputs["transport"] == "car" or inputs["transport"] == "motorcycle" or inputs["transport"] == "airplane":
        recs.append("Try public transport, biking, walking, or carpooling.")
    #this means eats more than 1 burger a week
    if inputs["meat_emissions"] > 0.5:
        recs.append("Reducing beef consumption can have a huge impact.")
    #the reccomended shower time is 7 minutes
    if inputs["shower_time"] > 7:
        recs.append("Shorten showers to save water and energy.")
    #still outputs something if recs are empty ie actions are not contributing sig to a high carbon footprint
    if not recs:
        recs.append("Keep up the great work! Here is a link to more suggestions to reduce your carbon footprint: https://www.un.org/en/actnow/ten-actions ")
    return recs
