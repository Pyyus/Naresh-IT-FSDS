#Import the streamlit
import streamlit as st

#Add title of your app
st.title("My First StreamLit App")

# Add some text
st.write("Welcome to My Calculator App. Here you find the square of any number between 0 to 100.")

# Create an interactive slider
st.header("Select the number")
number = st.slider("Pick a number",0,100,5)

#Calculate and Display the Result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of number **{number}** is **{squared_number}**.")