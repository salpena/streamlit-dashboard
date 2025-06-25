import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

st.title("🛳️ Titanic Passengers Dashboard")

st.markdown("Explore demographics, survival, and other details from the Titanic dataset. You can just say stuff!")

# Filters
pclass = st.selectbox("Passenger Class", options=["All"] + sorted(df["Pclass"].unique().tolist()))
sex = st.selectbox("Gender", options=["All"] + sorted(df["Sex"].unique().tolist()))

filtered_df = df.copy()
if pclass != "All":
    filtered_df = filtered_df[filtered_df["Pclass"] == int(pclass)]
if sex != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == sex]

st.write("Filtered Dataset", filtered_df)

# Survival Pie Chart
fig1 = px.pie(filtered_df, names="Survived", title="Survival Distribution")
st.plotly_chart(fig1)

# Age Distribution
fig2 = px.histogram(filtered_df, x="Age", nbins=30, title="Age Distribution")
st.plotly_chart(fig2)

# Gender Count
fig3 = px.histogram(filtered_df, x="Sex", title="Gender Count")
st.plotly_chart(fig3)
