import streamlit as st

st.title("Inflation Explorer")

st.write("This app shows how inflation affects the value of money over time.")

inflation_rate = st.slider("Annual inflation rate (%)", 0.0, 20.0, 3.0)
years = st.slider("Years in the future", 1, 30, 10)
current_value = st.number_input("Current money value (£)", value=100.0)

future_value = current_value / ((1 + inflation_rate / 100) ** years)

st.write(f"£{current_value:.2f} will be worth about £{future_value:.2f} in {years} years at {inflation_rate}% inflation.")