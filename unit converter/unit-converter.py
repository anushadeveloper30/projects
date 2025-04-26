#Basic Unit Converter using Streamlit
import streamlit as st
# Title and intro (commented out, can be enabled)
st.title("🌍 Welcome to Unit Converter App")
st.markdown("### This app converts units of length, weight, and time instantly.")
st.write("Welcome! select a category to convert units.")

# User selects category (Length, Weight, Time)
category = st.selectbox("Select a category", ["Length", "Weight", "Time"])

# Function to handle conversion logic
def convert_units(category, value, unit):
    # Length conversions
    if category == "Length":
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "miles to kilometer":
            return value / 0.621371
    # Weight conversions
    elif category == "Weight":
        if unit == "kilogram to pounds":
            return value * 2.20462
        elif unit == "pounds to kilogram":
            return value / 2.20462
    # Time conversions
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("Select a unit", ["miles to kilometer","kilometer to miles" ])
elif category == "Weight":
    unit = st.selectbox("Select a unit", ["kilogram to pounds", "pounds to kilogram"])
elif category == "Time":
    unit = st.selectbox("Select a unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

# User inputs the value to convert
value = st.number_input("Enter the value to convert")

# Convert button triggers the conversion
if st.button("Convert"):
    result = convert_units(category, value, unit)  # Call conversion function
    st.success(f"The converted value is: {result:.2f}")  # Display result