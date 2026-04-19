def get_recommendations(inputs):
    recs = []

    if inputs["transport"] == "car":
        recs.append("Try public transport, biking, or carpooling.")

    if inputs["meat_emissions"] > 0.67:
        recs.append("Reducing beef consumption can have a huge impact.")

    if inputs["shower_time"] > 10:
        recs.append("Shorten showers to save water and energy.")

    if recs is None:
        rec.append("Keep up the great work. Here is a link to more suggestions to reduce your carbon footprint: ")
    return recs
