def get_recommendations(inputs):
    recs = []

    if inputs["transport"] == "car" or inputs["transport"] == "motorcycle" or inputs["transport"] == "airplane":
        recs.append("Try public transport, biking, walking, or carpooling.")

    if inputs["meat_emissions"] > 0.67:
        recs.append("Reducing beef consumption can have a huge impact.")

    if inputs["shower_time"] > 7:
        recs.append("Shorten showers to save water and energy.")

    if not recs:
        recs.append("Keep up the great work! Here is a link to more suggestions to reduce your carbon footprint: https://www.un.org/en/actnow/ten-actions ")

    return recs
