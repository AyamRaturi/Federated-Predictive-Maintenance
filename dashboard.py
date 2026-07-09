import streamlit as st
import pandas as pd
import time

# 1. Main Heading
st.title("Federated Learning Predictive Maintenance")
st.write("Welcome to the visual dashboard. Watch the AI sensors update LIVE! 🚀")

# 2. Load Machine 1 Data
df1 = pd.read_csv("data/client_1.csv")

st.subheader("Machine 1 - LIVE Sensor Graph")

# 3. Create the starting point of the chart
live_chart = st.line_chart(df1[['temperature', 'vibration']].iloc[0:1])

# 4. Loop through the data to animate it
# We show 150 rows so the examiner can see the animation quickly
for i in range(1, 150):
    
    # Get the exact next row of data
    new_row = df1[['temperature', 'vibration']].iloc[i:i+1]
    
    # Add the new row to the moving chart
    live_chart.add_rows(new_row)
    
    # Pause for 0.1 seconds to create the live effect
    time.sleep(0.1)

# 5. Success Message when done
st.success("Live data stream complete!")