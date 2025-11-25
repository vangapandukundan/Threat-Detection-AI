import streamlit as st
import pandas as pd
import pickle

st.title("Threat Detection Using AI")

st.write("Upload a CSV file of network logs and the model will classify them.")

# File uploader
file = st.file_uploader("Upload CSV File", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write("Uploaded Data:")
    st.dataframe(df.head())

    # Load your trained ML model
    model = pickle.load(open("model.pkl", "rb"))

    # Make predictions
    predictions = model.predict(df)

    st.write("### Predictions:")
    st.write(predictions)
