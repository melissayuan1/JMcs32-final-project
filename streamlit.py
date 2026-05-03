#import streamlit (NEW)
import streamlit as st
# Import functions
from functions.dataload import load_data
from functions.recs import get_recommendations
from functions.calculate import calculate_transport, calculate_water, calculate_meat

# header section on streamlit
st.title("🌱Carbon Footprint Calculator🌱")
st.markdown("Calculate your daily CO₂ impact based on transport, meat, and water usage.")

# Load data -- creates a dictionary
transport_data = load_data('transport.csv', 'transportation', 'emissions')

# header for input section on streamlit
st.header("Daily Habits")

# Transportation
#use a dropdown for transportation options
transport = st.selectbox("Mode of transportation:", list(transport_data.keys()))
distance = st.number_input("Miles per day:", min_value=0.0, step=1.0)

# Shower
shower_time = st.number_input("Minutes per shower:", min_value=0.0, step=1.0)

# Meat Consumption
burgers_per_week = st.number_input("Burgers consumed per week:", min_value=0.0, step=1.0)

# Calculations
transport_emissions = calculate_transport(transport_data, transport, distance)
water_emissions = calculate_water(shower_time, 0.2)
meat_emissions = calculate_meat(burgers_per_week, 2.35)
total = transport_emissions + water_emissions + meat_emissions

# results section. if statement to print when user presses button
if st.button("Calculate My Footprint"):
    st.divider()
    #presents results for each individually
    st.header("Your Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Transport", f"{transport_emissions:.2f} kg")
    col2.metric("Shower", f"{water_emissions:.2f} kg")
    col3.metric("Meat", f"{meat_emissions:.2f} kg")

    #presents total results
    st.subheader(f"Total Daily CO₂: {total:.2f} kg")

    # Recommendations
    st.subheader("Suggestions for you:")
    inputs = {"transport": transport, "shower_time": shower_time, "meat_emissions": meat_emissions} #dictionary of category and user results
    recs = get_recommendations(inputs) #gets recs using these inputs

    #prints suggestions as a list
    for r in recs:
        st.info(r)
