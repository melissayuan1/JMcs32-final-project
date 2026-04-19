def get_recommendations(inputs):
    recs = []

    if inputs["transport"] == "car":
        recs.append("Try public transport, biking, or carpooling.")

    if meat > "beef":
        recs.append("Reducing beef consumption has a huge impact.")

    if inputs["shower_time"] > 10:
        recs.append("Shorten showers to save water and energy.")

    return recs
