import streamlit as st

st.title("Convert Between Fahrenheit and Celsius")


st.write("Enter a temperature and select the conversion direction.")

temp = st.number_input("Temperature:", value=0.0)
conversion_direction = st.selectbox("Convert to:", ("Celsius", "Fahrenheit"))

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def convert_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

if st.button("Convert"):
    if conversion_direction == "Celsius":
        converted = convert_to_celsius(temp)
        st.write(f"{temp} °F is {converted} °C")
    else:
        converted = convert_to_fahrenheit(temp)
        st.write(f"{temp} °C is {converted} °F")