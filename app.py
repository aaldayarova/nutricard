# Import necessary libraries
import pandas as pd
import streamlit as st

# Save .csv file into a dataset object using pandas library
df = pd.read_csv("cleaned-nutrition.csv")

# Create a dropdown menu containing our dataset "name" values
option = st.selectbox(
    "What grocery item would you like to add?", df["new_name"])

# Print the value chosen by the user
st.write('You selected:', option)

st.write(df.loc[df["new_name"] == option])
